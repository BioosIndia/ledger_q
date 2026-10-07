import sys,json,termios,secrets,datetime,urllib.request,urllib.error,http.cookiejar
from pathlib import Path
fd=sys.stdin.fileno();old=termios.tcgetattr(fd);new=list(old);new[3]&=~termios.ECHO;termios.tcsetattr(fd,termios.TCSANOW,new)
print('Ready for scoped credential on hidden stdin.',flush=True)
try: credential=json.loads(sys.stdin.readline())
finally: termios.tcsetattr(fd,termios.TCSANOW,old)
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs): return None
base='https://ledger-q.r4dewangan.chatgpt.site'
client=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()),NoRedirect())
csrf='';results=[]
def call(path,body=None):
 hdr={'OAI-Sites-Authorization':'Bearer '+credential['token']}
 data=None
 if body is not None:hdr.update({'Origin':base,'x-lq-csrf':csrf,'Content-Type':'application/json'});data=json.dumps(body).encode()
 req=urllib.request.Request(base+'/api/ledger/'+path,data=data,headers=hdr,method='POST' if data is not None else 'GET')
 try:
  with client.open(req,timeout=40) as response:return json.loads(response.read())
 except urllib.error.HTTPError as e: raise RuntimeError(path.split('?')[0]+' returned HTTP '+str(e.code))
def check(name,condition):
 if not condition:raise RuntimeError(name)
 results.append({'name':name,'result':'PASS'});print('PASS '+name,flush=True)
def entry():return call('workspaces/create',{'defaultEntry':True,'name':'Fresh hosted check','requestId':secrets.token_hex(20)})['workspaceId']
try:
 email='v5-entry-'+secrets.token_hex(8)+'@example.invalid';password=secrets.token_urlsafe(24)
 auth=call('signup',{'name':'Synthetic fresh-entry check','email':email,'password':password,'syntheticConsent':True});csrf=auth['csrf']
 sessions=call('session');wid=sessions['workspaces'][0]['id'];fresh=call('state?workspaceId='+wid)
 check('New hosted account contains no evidence, proof or jobs',fresh['state']['records']==[] and fresh['state']['jobs']==[] and not fresh['state']['workspace'].get('proofTemplate'))
 check('Default entry reuses that empty private workspace',entry()==wid)
 call('action',{'action':'load-proof','workspaceId':wid,'expectedRevision':fresh['revision'],'operationKey':secrets.token_hex(20),'proofId':'DRUG-Q-OOS','confirmSynthetic':True})
 proof=call('state?workspaceId='+wid)
 emptyId=entry();empty=call('state?workspaceId='+emptyId)
 check('Populated proof remains separate from the new zero-record entry',emptyId!=wid and empty['state']['records']==[] and empty['state']['jobs']==[] and not empty['state']['workspace'].get('proofTemplate'))
 check('Default entry never clears the existing proof',(call('state?workspaceId='+wid)['state']==proof['state']))
 call('logout',{});auth=call('login',{'email':email,'password':password});csrf=auth['csrf']
 check('Returning login can enter the same empty dashboard while saved proof stays available',entry()==emptyId and any(w['id']==wid and w.get('proofTemplate')=='DRUG-Q-OOS' for w in call('session')['workspaces']))
 call('logout',{});check('Hosted logout clears the app session',call('session')['user'] is None)
except Exception as e:
 results.append({'name':'Hosted entry verification','result':'BLOCKED_OR_FAILED','reason':str(e)[:200]});print(str(e)[:200],flush=True)
finally:
 report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Actual hosted API checks on purpose-created synthetic accounts. No browser UI, live provider calls, real user evidence or human approvals.','results':results,'passed':sum(r['result']=='PASS' for r in results)}
 Path('/workspace/scratch/61995385ee8d/verification-v5/hosted-results.json').write_text(json.dumps(report,indent=2));credential.clear()
