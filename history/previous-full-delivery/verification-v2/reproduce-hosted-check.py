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
  try: return Response(self.opener.open(req,timeout=kw.get('timeout',25)))
  except urllib.error.HTTPError as e: return Response(e)
 def get(self,url,**kw): return self.request('GET',url,**kw)
base='https://ledger-q.r4dewangan.chatgpt.site';client=Session();client.headers['OAI-Sites-Authorization']='Bearer '+credential['token'];results=[]
def call(path,body=None):
 headers={'Origin':base} if body is not None else {}
 response=client.request('POST' if body is not None else 'GET',base+'/api/ledger/'+path,json=body,headers=headers,allow_redirects=False,timeout=25)
 try: data=response.json()
 except: data={}
 if response.status_code!=200: raise RuntimeError('Endpoint '+path.split('?')[0]+' returned '+str(response.status_code)+': '+str(data.get('error','non-JSON/redirect response'))[:180])
 return data
def check(name,fn):
 fn();results.append({'name':name,'result':'PASS'});print('PASS '+name,flush=True)
try:
 check('Hosted bindings and encryption configuration',lambda: all(call('health').get(k) for k in ['storage','originals','encryption']) or (_ for _ in ()).throw(RuntimeError('Missing binding')))
 a=call('demo');b=call('demo')
 check('Hosted saved demo persists identical record identities',lambda: a['state']['records'][0]['id']==b['state']['records'][0]['id'] or (_ for _ in ()).throw(RuntimeError('Demo changed')))
 check('Hosted synthetic assay remains HOLD',lambda: next(r for r in b['state']['records'] if r['id']=='EVT-OOS-026')['status']=='HOLD' or (_ for _ in ()).throw(RuntimeError('Unsupported advancement')))
 response=client.get(base+'/api/ledger/demo-original?id=SRC-SOP-014',allow_redirects=False,timeout=25)
 check('Hosted source original readback',lambda: response.status_code==200 and 'acceptance' in response.text.lower() or (_ for _ in ()).throw(RuntimeError('Original unavailable')))
 account=call('signup',{'name':'Automated synthetic delivery check','email':'delivery-check-'+secrets.token_hex(7)+'@example.invalid','password':secrets.token_urlsafe(24),'syntheticConsent':True});client.headers['x-lq-csrf']=account['csrf']
 session=call('session');wid=session['workspaces'][0]['id'];st=call('state?workspaceId='+wid)
 check('Hosted app-owned sign-in advances into saved workspace',lambda: st['state']['workspace']['id']==wid or (_ for _ in ()).throw(RuntimeError('Workspace unavailable')))
 op=secrets.token_hex(20);body={'action':'source','workspaceId':wid,'expectedRevision':st['revision'],'operationKey':op,'title':'Delivery check — synthetic source','text':'The operator must preserve the original value.','purpose':'Authorized synthetic delivery verification','permission':True}
 created=call('action',body);st2=call('state?workspaceId='+wid)
 check('Hosted source save is persisted',lambda: any(r['id']==created['recordId'] for r in st2['state']['records']) or (_ for _ in ()).throw(RuntimeError('Save missing')))
 replay=call('action',body)
 check('Hosted duplicate operation replays without a duplicate save',lambda: replay.get('replayed') is True or (_ for _ in ()).throw(RuntimeError('Not idempotent')))
 call('logout',{});logged=call('session')
 check('Hosted logout ends app session',lambda: logged['user'] is None or (_ for _ in ()).throw(RuntimeError('Session still active')))
except Exception as e:
 results.append({'name':'Hosted verification','result':'BLOCKED_OR_FAILED','reason':str(e)[:250]});print('Verification gap: '+str(e)[:250],flush=True)
finally:
 report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Hosted HTTP API verification, not browser visual or professional validation. Test account/workspace contains explicitly synthetic delivery-check records only.','results':results,'passed':sum(x['result']=='PASS' for x in results)}
 Path('/workspace/scratch/61995385ee8d/ledger-q-hosted-results.json').write_text(json.dumps(report,indent=2));credential.clear()
