from pathlib import Path
import json,subprocess,shutil
R=Path(__file__).parent;M=R.parent/'media';D=json.loads((R/'scenes.json').read_text());receipts=[]
for p,data in D.items():
 for lang in ('en','hi'):
  parts=[];vtt=['WEBVTT',''];transcript=[f"# {data['name']} - {'English' if lang=='en' else 'Hindi'} narrated guide",'', 'Animated explanation of the saved synthetic fixture; not live screen footage or a latency/accuracy benchmark.','']
  for i,s in enumerate(data['scenes']):
   src=M/f'{p}-{lang}-{i}.mp3';dest=M/f'{p}-{lang}-{i}.wav';parts.append(dest)
   dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(src)]))
   assert dur<14.9,(p,lang,i,dur)
   subprocess.run(['ffmpeg','-v','error','-y','-i',str(src),'-af','apad,atrim=duration=15','-ar','48000','-ac','1',str(dest)],check=True)
   def time(t):return f'{int(t)//3600:02d}:{int(t)//60%60:02d}:{int(t)%60:02d}.000'
   # smaller spoken-caption cues keep readable line lengths; five equal timed clauses per scene
   words=s[lang].split();chunks=[words[j:j+8] for j in range(0,len(words),8)]
   for j,c in enumerate(chunks):
    start=i*15+.35+j*(dur/len(chunks));end=min(i*15+14.8,i*15+.35+(j+1)*(dur/len(chunks)))
    def ts(t):return f'{int(t)//60:02d}:{int(t)%60:02d}.{int((t%1)*1000):03d}'
    vtt.extend([f'{ts(start)} --> {ts(end)}',' '.join(c),''])
   transcript.extend([f'## {i*15:02d}s - {(i+1)*15:02d}s | {s["title"]}',s[lang],''])
  concat=M/f'{p}-{lang}-audio.txt';concat.write_text(''.join(f"file '{x}'\n" for x in parts))
  wav=M/f'{p}-{lang}-narration.wav';subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(concat),'-c','copy',str(wav)],check=True)
  video=M/f'{p}-walkthrough-{lang}.mp4'
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(M/f'{p}-visual.mp4'),'-i',str(wav),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','128k','-af','loudnorm=I=-16:TP=-1.5:LRA=9','-t','120','-movflags','+faststart',str(video)],check=True)
  (M/f'{p}-walkthrough-{lang}.vtt').write_text('\n'.join(vtt))
  (M/f'{p}-transcript-{lang}.md').write_text('\n'.join(transcript))
  probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]))
  assert abs(float(probe['format']['duration'])-120)<.05
  stream=next(x for x in probe['streams'] if x['codec_type']=='video');assert stream['width']==1920 and stream['height']==1080 and stream['avg_frame_rate']=='30/1'
  assert any(x['codec_type']=='audio' for x in probe['streams'])
  receipts.append({'file':video.name,'seconds':120,'width':1920,'height':1080,'fps':30,'audio':'AAC, English or Hindi neural narration','bytes':video.stat().st_size,'captionTiming':'Scene-aligned phrase captions; not word-level forced alignment','scope':'Animated saved synthetic-case guide, not browser recording or measured product latency'})
(M/'video-verification.json').write_text(json.dumps(receipts,indent=2))
print('Verified four 120-second 1080p30 narrated MP4s')
