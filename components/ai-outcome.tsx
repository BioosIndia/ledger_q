import type {Item} from '@/lib/ledger/types';
import {savedOutcome} from '@/lib/ledger/outcome';
import {Button} from '@/components/ui/button';

export function AIOutcome({job,records,inspect}:{job:any;records:Item[];inspect:(r:Item)=>void}) {
  const result=savedOutcome(job,records);
  function download(){const lines=['LEDGER-Q — unapproved run review brief',`Target: ${job.targetId} · input version ${job.targetVersion}`,`Current state: ${result.state}`,`Execution: ${result.execution}`,'Not a controlled export, QA disposition or release decision.','','SUPPORTED FINDINGS',...result.supported.flatMap(f=>[f.statement,`Source: ${f.sourceId} · v${f.version}`]),'','EVIDENCE GAPS',...result.gaps,'','NEXT ACTION',result.nextAction,'','Human review required. Automatic release: false.'];const url=URL.createObjectURL(new Blob([lines.join('\n')],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download=`ledger-q-${job.targetId}-v${job.targetVersion}-review.txt`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
  return <section aria-label="Saved AI outcome">
    <h3>What this run found</h3>
    <p><strong>{result.state}</strong> · {result.execution}</p>
    <p>{result.target?.title||'Target unavailable'} · input version {job.targetVersion||'Not recorded'} · current version {result.target?.version||'Unavailable'}</p>
    <h4>Supported findings</h4>
    {result.supported.length?<ul>{result.supported.map((f,i)=><li key={f.sourceId+':'+i}>
      <p>{f.statement}</p><Button className="btn white" onClick={()=>{const source=records.find(r=>r.id===f.sourceId);if(source)inspect(source);}}>Inspect {f.sourceId} · v{f.version}</Button>
    </li>)}</ul>:<p>No current source-backed finding passed these checks. Missing values are not filled in.</p>}
    <h4>What prevents progression</h4>
    {result.gaps.length?<ul>{result.gaps.map((gap,i)=><li key={i}>{gap}</li>)}</ul>:<p>No gap detected by these bounded checks. Qualified human review is still required.</p>}
    {result.suggestions.length>0&&<><h4>Specialist suggestions — not established facts</h4><ul>{result.suggestions.map((s,i)=><li key={i}><strong>{s.specialist}: </strong>{s.text}</li>)}</ul><p className="micro">These are candidate next steps. A human must confirm suitability; they do not establish root cause, disposition or CAPA effectiveness.</p></>}
    <h4>Next responsible action</h4><p>{result.nextAction}</p>
    <Button className="btn white" onClick={download}>Download unapproved review brief</Button><p className="micro">Use Audit / export for a saved evidence packet with its revision, approval state and integrity record.</p>
    <p className="micro">{result.received} successful provider response(s) recorded{result.models.length?' · '+result.models.join(' / '):''}. Saved execution is not a real-user benefit or accuracy study. Automatic release: false.</p>
    <details><summary>Inspect the technical run receipt</summary><pre className="source-text">{JSON.stringify(job,null,2)}</pre></details>
  </section>;
}
