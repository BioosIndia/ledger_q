from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import textwrap,html,re
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,Image as PDFImage,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
B=Path('/workspace/scratch/61995385ee8d/delivery-2026-10-06');L=B/'LEDGER_Q_Planning_Package'
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
im=Image.new('RGB',(1600,2030),'#172738');d=ImageDraw.Draw(im)
def txt(x,y,t,size=28,color='#eff4f8',bold=False):d.text((x,y),t,font=ImageFont.truetype(FB if bold else F,size),fill=color)
def box(x,y,w,h,title,body,col='#26465c'):
 d.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=col,outline='#69c5d8',width=2)
 for j,l in enumerate(textwrap.wrap(title,int(w/17))):txt(x+22,y+14+j*35,l,29,'#91e1ee',True)
 # body explicit one or two lines starting at y+74
 for j,l in enumerate(textwrap.wrap(body,int(w/14))):txt(x+22,y+78+j*30,l,24)
def arr(points,col='#8cdceb'):
 d.line(points,fill=col,width=4);x,y=points[-1];px,py=points[-2];
 if y>py:d.polygon([(x,y),(x-9,y-16),(x+9,y-16)],fill=col)
 elif y<py:d.polygon([(x,y),(x-9,y+16),(x+9,y+16)],fill=col)
 elif x>px:d.polygon([(x,y),(x-16,y-9),(x-16,y+9)],fill=col)
 else:d.polygon([(x,y),(x+16,y-9),(x+16,y+9)],fill=col)
txt(70,35,'LEDGER-Q · Two streams, one human authority',37,bold=True);txt(70,88,'Planning from PDF p1–16 · not an implemented or validated product',24,'#c6d5df')
box(70,155,1460,140,'Permitted intake and versioned originals · L01–L05','Tenant / role / purpose → exact source version, hash, coordinates and context')
arr([(800,295),(800,335),(385,335),(385,375)]);arr([(800,335),(1215,335),(1215,375)])
box(70,375,630,145,'QUALITY · F01–F04','Source → requirement → SOP mapping → visible gap / conflict')
box(900,375,630,145,'AI ASSURANCE · F16–F17','Model / use / context → pinned provenance and contribution')
arr([(385,520),(385,555)]);arr([(1215,520),(1215,555)])
box(70,555,630,165,'F05–F10 / F13','Risk, deviation, OOS/OOT → candidate RCA / CAPA / change → training / owner')
box(900,555,630,165,'F18–F19','Frozen grounding / hallucination / bias / edge / consistency / paired tests')
arr([(385,720),(385,760),(800,760),(800,805)]);arr([(1215,720),(1215,760),(800,760)])
box(270,805,1060,145,'SHARED EVIDENCE GRAPH · L06–L07','Exact dependencies, current revision, source sufficiency and assurance debt')
arr([(800,950),(800,1000)])
box(470,1000,660,130,'Current + sufficient evidence?','Missing / stale / conflicting → UNKNOWN / HOLD',col='#3c4150')
box(70,1175,450,180,'NO · HOLD','Request evidence / owner action; no unsupported conclusion',col='#58402d')
box(635,1175,895,180,'YES · Named QA review / signing · F14','Role + Password + OTP (or approved biometric second factor) + reason + exact revision/hash')
arr([(640,1130),(300,1153),(300,1175)],'#ffc778');arr([(950,1130),(1080,1153),(1080,1175)])
arr([(1080,1355),(1080,1400)])
box(635,1400,895,165,'Decision → effectiveness / inspection / trends','F09 / F11–F12: human authority; effectiveness evidence required before closure')
arr([(1080,1565),(1080,1610)])
box(635,1610,895,145,'F15 · Exact-version replay / passport / export','Original source + run + decision history retained; controlled packet')
arr([(1080,1755),(1080,1800)])
box(635,1800,895,145,'F08 / F20 · Monitor, change and revalidation','Affected assurance stale → reopen → retest → fresh named human approval')
arr([(635,1860),(15,1860),(15,875),(270,875)])
arr([(70,1260),(38,1260),(38,220),(70,220)],'#ffc778')
txt(70,1970,'Parent runtime · L08–L12: bounded specialists, 3 retries, DLQ/manual continuity, audit.',22,'#c6d5df')
im.save(L/'LEDGER_Q_Master_Architecture.png')
# Readable Markdown-to-PDF export; retain exact table rows without truncation.
pdfmetrics.registerFont(TTFont('DejaVu',F));pdfmetrics.registerFont(TTFont('DejaVuBold',FB))
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='Bodyx',fontName='DejaVu',fontSize=9.6,leading=14,spaceAfter=7));styles.add(ParagraphStyle(name='Hx',fontName='DejaVuBold',fontSize=16,leading=21,spaceBefore=14,spaceAfter=9));styles.add(ParagraphStyle(name='Smallx',fontName='DejaVu',fontSize=7.4,leading=10));styles.add(ParagraphStyle(name='Titlex',fontName='DejaVuBold',fontSize=24,leading=30,spaceAfter=18))
def rich(s):
 s=html.escape(s);s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s);s=re.sub(r'`([^`]+)`',r'<font color="#245367">\1</font>',s);return s

def make(md,pdf,title,overview=False):
 doc=SimpleDocTemplate(str(pdf),pagesize=(595,842),rightMargin=36,leftMargin=36,topMargin=43,bottomMargin=43,title=title,author='Rahul Dewangan / PRAMANEX')
 story=[Paragraph(title,styles['Titlex']),Paragraph('6 October 2026 · Planning handoff · LEDGER-Q application not built in this task',styles['Bodyx']),Spacer(1,12)]
 if overview:story += [PDFImage(str(L/'LEDGER_Q_Master_Architecture.png'),width=480,height=609),PageBreak()]
 lines=md.read_text().splitlines();i=0
 while i<len(lines):
  s=lines[i].strip()
  if not s:i+=1;continue
  if s.startswith('```'):
   kind=s[3:];code=[];i+=1
   while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
   if kind=='mermaid':story.append(Paragraph('Editable branched flowchart is supplied in the Markdown and matching .mmd file. The overview diagram is included above.',styles['Bodyx']))
   else:story.append(Paragraph('<br/>'.join(html.escape(c) for c in code),styles['Smallx']))
   i+=1;continue
  if s.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    parts=[x.strip() for x in lines[i].strip().strip('|').split('|')]
    if not all(re.match(r'^:?-+:?$',x) for x in parts):rows.append(parts)
    i+=1
   n=max(len(r) for r in rows);data=[[Paragraph(rich(x),styles['Smallx']) for x in r]+['']*(n-len(r)) for r in rows]
   widths=[523/n]*n
   if n==5:widths=[105,74,77,105,162]
   if n==4:widths=[110,125,130,158]
   table=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT');table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dcecf2')),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#bdcbd4')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story += [table,Spacer(1,12)];continue
  if s.startswith('# '):i+=1;continue
  if s.startswith('## '):story.append(Paragraph(rich(s[3:]),styles['Hx']));i+=1;continue
  if s.startswith('### '):story.append(Paragraph(rich(s[4:]),styles['Hx']));i+=1;continue
  group=[s];i+=1
  # Keep bullets and numbered items as individual paragraphs.
  if not re.match(r'^[-\d]',s):
   while i<len(lines) and lines[i].strip() and not lines[i].strip().startswith(('#','|','```','- ')):
    group.append(lines[i].strip());i+=1
  story.append(Paragraph(rich(' '.join(group)),styles['Bodyx']))
 def footer(c,d):c.setFont('DejaVu',8);c.setFillColor(colors.HexColor('#4b6476'));c.drawString(36,23,'PRAMANEX LEDGER-Q · Specified / not built in this planning task');c.drawRightString(559,23,str(d.page))
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
make(L/'LEDGER_Q_Master_Rulebook.md',L/'LEDGER_Q_Master_Rulebook.pdf','LEDGER-Q Master Rulebook')
make(L/'LEDGER_Q_Full_Mapping_and_Flowcharts.md',L/'LEDGER_Q_Full_Mapping_and_Flowcharts.pdf','LEDGER-Q PDF + Video Mapping',True)
print('Readable PDFs and precise master diagram created')
