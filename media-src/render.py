"""Reproducible animated guide, not browser capture or performance benchmark.
Requires Python Pillow and ffmpeg. Source facts are documented in scenes.json.
"""
from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import json,subprocess,math,sys,shutil
ROOT=Path(__file__).parent;OUT=ROOT.parent/'media';OUT.mkdir(exist_ok=True)
DATA=json.loads((ROOT/'scenes.json').read_text());project=sys.argv[1];item=DATA[project]
W,H=1920,1080
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n,b=False):return ImageFont.truetype(BOLD if b else FONT,n)
def text(draw,xy,content,size=26,color='#c7d1d0',bold=False):draw.text(xy,content,font=font(size,bold),fill=color)
accent=item['accent'];bg='#101d22' if project=='forge' else '#243b3b';card='#1b3034' if project=='forge' else '#314b49'
nav=['Originals','Facts','Gaps & conflicts','Module 3','Quality checks','Human review','Audit / output'] if project=='forge' else ['Workspace','Sources','Quality events','Investigation','CAPA','AI assurance','Review / audit']
paths=[]
for i,scene in enumerate(item['scenes']):
 im=Image.new('RGB',(W,H),bg);d=ImageDraw.Draw(im)
 d.rounded_rectangle((48,32,1872,100),20,fill=card)
 d.ellipse((73,52,103,82),outline=accent,width=3);d.line((82,67,95,67),fill=accent,width=3)
 text(d,(119,44),item['name'],30,accent,True);text(d,(1500,54),'PRAMANEX / RAHUL',19,'#d2ded8')
 text(d,(68,143),'TWO-MINUTE WORKFLOW GUIDE',19,accent,True)
 text(d,(68,180),item['subtitle'],46,'#f1f3ee',True)
 text(d,(68,244),'Animated explanation of the saved synthetic fixture. Not live screen footage.',23)
 # compact mock workflow frame is explicitly an explanatory reconstruction
 d.rounded_rectangle((64,304,1856,916),22,fill=card,outline='#577271',width=1)
 d.rounded_rectangle((88,329,365,886),14,fill='#12292e')
 text(d,(115,357),'WORKFLOW',19,accent,True)
 for j,n in enumerate(nav):
  y=414+j*60
  if j==min(max(i-1,0),6):d.rounded_rectangle((104,y-9,347,y+38),10,fill='#315e60')
  text(d,(120,y),n,20,'#e5ece7')
 text(d,(394,334),f'{i+1:02d} / 08',20,accent,True)
 text(d,(394,375),scene['title'],38,'#f1f3ee',True)
 d.rounded_rectangle((397,439,1785,484),12,fill='#43594e' if 'HOLD' not in scene['tag'] else '#795949')
 text(d,(420,446),scene['tag'],20,'#fcf3df',True)
 for k,line in enumerate(scene['lines']):
  y=529+k*95
  d.rounded_rectangle((397,y-4,1785,y+65),12,fill='#203c40')
  d.ellipse((418,y+15,438,y+35),fill=accent)
  text(d,(456,y+11),line,24,'#edf0e9',k==0)
 # intact boundary consistently visible
 text(d,(399,838),'No critical value invented. No autonomous regulatory release.',22,accent)
 # timeline chapters as eight pills
 for j in range(8):
  x=68+j*226
  d.rounded_rectangle((x,951,x+208,967),7,fill=accent if j<=i else '#415655')
 text(d,(68,990),f'Chapter {i+1}/8  |  {i*15:02d}s - {(i+1)*15:02d}s',21,'#dae2dc')
 text(d,(1130,990),'SYNTHETIC CASE / HUMAN REVIEW REQUIRED',20,accent,True)
 base=OUT/f'{project}-scene-{i}.png';im.save(base)
 # directional cursor with soft edge; this only highlights, it does not fake live interaction
 cursor=Image.new('RGBA',(72,88),(0,0,0,0));cd=ImageDraw.Draw(cursor)
 cd.polygon([(5,4),(5,67),(22,51),(35,77),(48,69),(34,44),(58,44)],fill='#eff8f4',outline='#122629',width=3)
 cp=OUT/f'{project}-cursor.png';cursor.save(cp)
 clip=OUT/f'{project}-scene-{i}.mp4';paths.append(clip)
 # ease-in directional path toward highlighted source row, then gentle resting motion
 progress='min(t/5,1)';smooth=f'({progress})*({progress})*(3-2*({progress}))'
 x=f'1640-500*{smooth}+3*sin(t*0.7)';y=f'770-190*{smooth}+2*cos(t*0.7)'
 subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',str(base),'-loop','1','-i',str(cp),'-filter_complex',f'[0:v]setsar=1[bg];[bg][1:v]overlay=x=\'{x}\':y=\'{y}\':shortest=1,format=yuv420p[v]','-map','[v]','-t','15','-r','30','-c:v','libx264','-preset','veryfast','-crf','21','-threads','4','-an',str(clip)],check=True)
 print(project,'scene',i,'rendered',flush=True)
manifest=OUT/f'{project}-concat.txt';manifest.write_text(''.join(f"file '{p}'\n" for p in paths))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(manifest),'-c','copy',str(OUT/f'{project}-visual.mp4')],check=True)
# first frame poster and summary contact sheet for actual inspection
shutil.copy(OUT/f'{project}-scene-0.png',OUT/f'{project}-poster.png')
contact=Image.new('RGB',(1280,720),bg)
for i in range(8):
 thumbnail=Image.open(OUT/f'{project}-scene-{i}.png');thumbnail.thumbnail((320,360));contact.paste(thumbnail,((i%4)*320,(i//4)*360+80))
contact.save(OUT/f'{project}-contact-sheet.jpg')
print(project,'visual master complete',flush=True)
