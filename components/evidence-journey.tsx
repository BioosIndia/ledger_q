import type {Item} from '@/lib/ledger/types';

/** Decorative layers are independent of saved workflow data. */
export function EvidenceMotion({priority=false}:{priority?:boolean}){
 return <div className="evidence-motion" aria-hidden="true"><div className="motion-floor"/><div className="motion-orbit orbit-one"/><div className="motion-orbit orbit-two"/><div className="motion-sculpture"><span className="depth-plane plane-back"/><img src="/evidence-gate-v2.webp" width="1536" height="1024" alt="" loading={priority?'eager':'lazy'} fetchPriority={priority?'high':'auto'}/><span className="depth-plane plane-front"/><span className="motion-signal signal-source"/><span className="motion-signal signal-review"/><span className="motion-signal signal-history"/></div></div>;
}
export function EvidenceJourney({records,revision,link}:{records:Item[];revision:number;link:(screen:string)=>string}){
 const sources=records.filter(r=>r.kind==='controlled_sources');
 const gaps=records.filter(r=>r.gaps.length);
 const decisions=records.filter(r=>r.kind==='human_decisions');
 const packets=records.filter(r=>r.kind==='exports');
 const first=!sources.length?'sources':gaps.length?'events':!decisions.length?'review':'audit';
 const next=!sources.length?'Add an original source':gaps.length?'Inspect gaps before requesting review':!decisions.length?'Request named review of the exact revision':'Inspect decisions and packet status';
 const steps=[{screen:'sources',title:'Original evidence',value:sources.length,copy:'Saved source records'},{screen:'events',title:'Visible uncertainty',value:gaps.length,copy:'Records with unresolved gaps'},{screen:'review',title:'Human decisions',value:decisions.length,copy:'Recorded history, not current approval'},{screen:'audit',title:'Evidence packets',value:packets.length,copy:'Inspect each packet’s approval state'}];
 return <section className="outcome-journey reveal" aria-label="Saved evidence and next action"><div className="outcome-heading"><div><span className="eyebrow">YOUR SAVED EVIDENCE THREAD · r{revision}</span><h2>What is recorded. What comes next.</h2></div><a className="btn dark inline" href={link(first)}>{next}<span aria-hidden="true">↗</span></a></div><ol>{steps.map((s,i)=><li key={s.screen}><a href={link(s.screen)}><span className="journey-index">0{i+1}</span><div><h3>{s.title}</h3><b className="outcome-count">{s.value}</b><p>{s.copy}</p></div><span aria-hidden="true">↗</span></a></li>)}</ol><p className="micro">Counts come from this workspace. Decisions may be historical; changed evidence requires fresh review. A saved packet is not automatically approved.</p></section>;
}
