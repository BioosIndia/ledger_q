import sys,json,termios,secrets,datetime,urllib.request,urllib.error,http.cookiejar
from pathlib import Path
fd=sys.stdin.fileno();old=termios.tcgetattr(fd);new=list(old);new[3]&=~termios.ECHO;termios.tcsetattr(fd,termios.TCSANOW,new)
print('Ready for scoped service credential on hidden stdin.',flush=True)
try: credential=json.loads(sys.stdin.readline())
finally: termios.tcsetattr(fd,termios.TCSANOW,old)
class Response:
 def __init__(self,r): self.status_code=r.code;self.text=r.read().decode('utf-8',errors='replace')
 def json(self): return json.loads(self.text)
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs): return None
class Session:
 def __init__(self): self.headers={};self.opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()),NoRedirect())
 def request(self,method,url,json=None,headers=None,**kw):
  hdr={**self.headers,**(headers or {})};data=None
  if json is not None: data=__import__('json').dumps(json).encode();hdr['Content-Type']='application/json'
  req=urllib.request.Request(url,data=data,headers=hdr,method=method)
  try: return Response(self.opener.open(req,timeout=kw.get('timeout',180)))
  except urllib.error.HTTPError as e: return Response(e)
 def get(self,url,**kw): return self.request('GET',url,**kw)
base='https://ledger-q.r4dewangan.chatgpt.site';client=Session();client.headers['OAI-Sites-Authorization']='Bearer '+credential['token'];results=[]
def call(path,body=None):
 headers={'Origin':base} if body is not None else {}
 response=client.request('POST' if body is not None else 'GET',base+'/api/ledger/'+path,json=body,headers=headers,allow_redirects=False,timeout=180)
 try: data=response.json()
 except: data={}
 if response.status_code!=200: raise RuntimeError('Endpoint '+path.split('?')[0]+' returned '+str(response.status_code)+': '+str(data.get('error','non-JSON/redirect response'))[:180])
 return data
def check(name,fn):
 fn();results.append({'name':name,'result':'PASS'});print('PASS '+name,flush=True)
try:
 account=call('signup',{'name':'Synthetic v3 QA check','email':'v3-check-'+secrets.token_hex(8)+'@example.invalid','password':secrets.token_urlsafe(24),'syntheticConsent':True});client.headers['x-lq-csrf']=account['csrf']
 session=call('session');wid=session['workspaces'][0]['id'];st=call('state?workspaceId='+wid)
 check('New hosted account starts with an empty private workspace',lambda: st['state']['records']==[] and st['state']['jobs']==[] and wid!='LQ-PUBLIC' or (_ for _ in ()).throw(RuntimeError('Account prepopulated')))
 def action(name,extra=None):
  current=call('state?workspaceId='+wid)
  return call('action',{'action':name,'workspaceId':wid,'expectedRevision':current['revision'],'operationKey':secrets.token_hex(20),**(extra or {})})
 selected=action('load-proof',{'proofId':'DRUG-Q-OOS','confirmSynthetic':True});st=call('state?workspaceId='+wid)
 check('Explicit proof selection persists a separate private copy',lambda: selected.get('proofLoaded') and st['state']['workspace'].get('proofTemplate')=='DRUG-Q-OOS' and all(r['fields']['objectKey'].startswith(wid+'/') for r in st['state']['records'] if r['kind']=='controlled_sources') or (_ for _ in ()).throw(RuntimeError('Selected proof missing or not isolated')))
 check('Gemini native key is configured without exposing its value',lambda: st.get('geminiConfigured') is True or (_ for _ in ()).throw(RuntimeError('Gemini key presence missing')))
 connected=action('connect-gemini',{'providerConsent':True});st=call('state?workspaceId='+wid)
 connection=next(r for r in st['state']['records'] if r['id']==connected['recordId'])
 results.append({'name':'Resolved Gemini identity receipt','result':'PASS' if connected.get('connected') else 'FAILED','models':connected.get('models'), 'actualModels':[o.get('actualModel') for o in connection['fields']['observations']], 'observations':connection['fields']['observations']})
 if not connected.get('connected'):
  results.append({'name':'Actual Gemini connection checks','result':'FAILED','models':connected.get('models',[]),'state':connection['status'],'observations':connection['fields']['observations']})
  print('Gemini connection checks failed; saved results retained.',flush=True)
 else:
  check('Two distinct actual Gemini models respond and saved readback verifies both',lambda: len(set(connected['models']))==2 and all(o['pass'] for o in connection['fields']['observations'] if o['model'] in connected['models']) and len(set(o.get('actualModel') for o in connection['fields']['observations'] if o['model'] in connected['models']))==2 or (_ for _ in ()).throw(RuntimeError('Two models not verified')))
  run=action('agent',{'id':'EVT-OOS-026','mode':'live'});st=call('state?workspaceId='+wid);job=next(j for j in st['state']['jobs'] if j['id']==run['runId'])
  check('Actual Gemini planner-specialist-review run saves checkpoints and human HOLD',lambda: job['phase']==4 and job['status']=='HOLD' and job['mode']=='Live AI' and job.get('reviewer',{}).get('independence',{}).get('pass') is True and isinstance(job.get('reviewer',{}).get('output',{}).get('supported'),bool) and len(job['outputs'])>=1 and any(a.get('provider')=='gemini' and a['status']=='RECEIVED' for a in job['attempts']) or (_ for _ in ()).throw(RuntimeError('Live team did not complete safely')))
  results.append({'name':'Actual Gemini saved run receipt','result':'PASS','workspaceId':wid,'runId':run['runId'],'status':job['status'],'phase':job['phase'],'specialists':job['plan'],'models':connected['models'],'attemptCount':len(job['attempts']),'tokens':[a.get('tokens') for a in job['attempts'] if a.get('tokens')]})
 fresh=call('workspaces/create',{'name':'QA fresh separation check','requestId':secrets.token_hex(20)});empty=call('state?workspaceId='+fresh['workspaceId'])
 check('Another explicitly created workspace stays fresh after proof and AI work',lambda: empty['state']['records']==[] and empty['state']['jobs']==[] or (_ for _ in ()).throw(RuntimeError('Proof leaked to new workspace')))
 call('logout',{});logged=call('session')
 check('Hosted logout invalidates session',lambda: logged['user'] is None or (_ for _ in ()).throw(RuntimeError('Session still active')))
except Exception as e:
 results.append({'name':'Hosted verification','result':'BLOCKED_OR_FAILED','reason':str(e)[:250]});print('Verification gap: '+str(e)[:250],flush=True)
finally:
 report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Actual hosted HTTP API checks and synthetic-only provider tests. No browser visual or qualified professional validation. Only purpose-created synthetic QA accounts/workspaces; no real user impersonation or human approval.','results':results,'passed':sum(x['result']=='PASS' for x in results)}
 Path('/workspace/scratch/61995385ee8d/verification-v3/hosted-results.json').write_text(json.dumps(report,indent=2));credential.clear()
