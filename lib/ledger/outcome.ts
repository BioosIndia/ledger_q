import type {Item} from './types';

type Fact = {sourceId:string;version:number;statement:string;span:string};
/** Read-only projection of a saved run. It neither calls a provider nor grants approval. */
export function savedOutcome(job:any, records:Item[]) {
  const target=records.find(r=>r.id===job?.targetId);
  const gaps=new Set<string>();
  const supported:Fact[]=[];
  const suggestions:Array<{specialist:string;text:string}>=[];
  let rejected=0;
  const stale=!target || target.version!==job?.targetVersion;
  if(stale)gaps.add('The target changed or is unavailable. Run again against the current evidence.');
  for(const gap of target?.gaps||[])gaps.add(gap);
  for(const id of target?.sourceIds||[]){
    const source=records.find(r=>r.id===id);
    if(!source)gaps.add('Linked evidence '+id+' is missing.');
    else {if(source.status!=='CURRENT')gaps.add('Linked evidence '+id+' is '+source.status+'.');for(const gap of source.gaps||[])gaps.add('Linked evidence '+id+': '+gap);}
  }
  const outputs=Array.isArray(job?.outputs)?job.outputs:[];
  for(const contribution of outputs){
    const value=job?.mode==='Live AI'?contribution.output:contribution;
    if(!value || !Array.isArray(value.facts)){gaps.add('A specialist has no complete structured evidence result.');continue;}
    for(const gap of Array.isArray(value.gaps)?value.gaps:[])if(typeof gap==='string'&&gap.trim())gaps.add(gap);
    for(const f of value.facts){
      const source=records.find(r=>r.id===f?.sourceId&&r.kind==='controlled_sources');
      const linked=target?.kind==='ai_uses'||target?.sourceIds.includes(f?.sourceId);
      const statement=job?.mode==='Live AI'?f?.statement:f?.span;
      const valid=!stale&&linked&&source&&source.version===f?.version&&typeof statement==='string'&&typeof f?.span==='string'
        &&f.span.trim().length>0&&statement===f.span&&String(source.fields.text||'').includes(f.span)
        &&source.status==='CURRENT'&&source.gaps.length===0;
      if(!valid){rejected++;continue;}
      if(!supported.some(x=>x.sourceId===f.sourceId&&x.version===f.version&&x.span===f.span))supported.push({sourceId:f.sourceId,version:f.version,statement,span:f.span});
    }
    if(typeof value.recommendation==='string'&&value.recommendation.trim())suggestions.push({specialist:String(contribution.specialist||'Specialist'),text:value.recommendation});
  }
  if(rejected)gaps.add(rejected+' candidate citation(s) failed current-source checks. They are excluded from supported findings.');
  if(!supported.length)gaps.add('No current, exact source-backed finding is available from this run.');
  const attempts=Array.isArray(job?.attempts)?job.attempts:[];
  const received=attempts.filter((a:any)=>a.status==='RECEIVED');
  const models=[...new Set(received.map((a:any)=>String(a.actualModel||a.model||'')).filter(Boolean))];
  const live=job?.mode==='Live AI';
  const providerFailure=live&&job?.status==='EXHAUSTED';
  if(providerFailure)gaps.add('The provider did not complete the saved run. The available passages remain candidates; no completed independent review is claimed.');
  const review=job?.reviewer?.output;
  const reviewPass=live&&job?.reviewer?.independence?.pass===true&&review?.supported===true&&Array.isArray(review.conflicts)
    &&Array.isArray(review.gaps)&&review.conflicts.length===0&&review.gaps.length===0;
  if(live&&!received.length)gaps.add('No successful provider response is recorded. Configuration alone is not live execution.');
  if(live&&received.length&&models.length<2)gaps.add('Distinct successful author and reviewer model identities are not recorded.');
  if(live&&!reviewPass)gaps.add('An independent model review has not passed for this saved candidate.');
  if(job?.phase!==4||!['HOLD','HUMAN_REVIEW_REQUIRED'].includes(job?.status))gaps.add('This run has not completed its evidence and review stages.');
  if(job?.status==='HOLD'&&!gaps.size)gaps.add('The saved run remains on HOLD. Inspect its review and re-planning receipt before progressing.');
  return {target,stale,supported,rejected,suggestions,gaps:[...gaps],models,received:received.length,
    execution:live?(received.length?'Live AI responses recorded':'Live AI not demonstrated'):'Deterministic source checks',
    state:stale?'STALE':gaps.size||job?.status==='HOLD'?'HOLD':'HUMAN REVIEW REQUIRED',
    nextAction:stale?'Select the current target and rerun the evidence checks.':providerFailure?'Restore provider availability or choose an accessible independent reviewer and resume the saved run. The listed evidence gaps still require human resolution.':gaps.size?'Resolve the listed evidence gaps with the named investigator or reviewer, then rerun.':'Ask the named QA reviewer to inspect the exact source revision and candidate; no approval has been granted.',
    release:false as const};
}
