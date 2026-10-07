import asyncio,json,ssl,subprocess,pathlib,sys,hashlib
import edge_tts
import edge_tts.communicate as transport
transport._SSL_CTX=ssl.create_default_context(cafile='/etc/ssl/certs/ca-certificates.crt')
ROOT=pathlib.Path(__file__).parent
DATA=json.loads((ROOT/'scenes.json').read_text())
OUT=ROOT.parent/'media';OUT.mkdir(exist_ok=True)
async def run():
 voices={'en':'en-IN-PrabhatNeural','hi':'hi-IN-MadhurNeural'}
 sem=asyncio.Semaphore(2)
 async def take(project,language,i,scene):
  async with sem:
   dest=OUT/f'{project}-{language}-{i}.mp3'
   stamp=dest.with_suffix(".sha256"); signature=hashlib.sha256(scene[language].encode()).hexdigest()
   if not dest.exists() or not stamp.exists() or stamp.read_text()!=signature:
    for attempt in range(3):
     try:
      await edge_tts.Communicate(scene[language],voices[language]).save(str(dest));stamp.write_text(signature);break
     except Exception:
      if attempt==2:raise
   duration=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(dest)]))
   if duration>14.9:print(f'OVERLONG {dest.name}: {duration:.2f}s',flush=True)
   return {'project':project,'language':language,'scene':i,'seconds':duration,'voice':voices[language]}
 results=await asyncio.gather(*(take(p,l,i,s) for p,x in DATA.items() for l in voices for i,s in enumerate(x['scenes'])))
 (OUT/'narration-timing.json').write_text(json.dumps(results,indent=2))
 assert max(x['seconds'] for x in results)<14.9, 'Shorten overlong scripts; never time-stretch narration'
 print('Saved and checked',len(results),'narration takes')
asyncio.run(run())
