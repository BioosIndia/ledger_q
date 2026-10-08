import type {State,Item} from './types';
const validDate=(v:unknown)=>typeof v==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(v)&&Number.isFinite(Date.parse(v))&&new Date(v).toISOString().slice(0,10)===v;
const present=(value:unknown)=>typeof value==='string'&&value.trim().length>=3;
export function causeIssues(r:Item){
 const f=r.fields,out:string[]=[];
 if(!['CONFIRMED','LIKELY','UNRESOLVED'].includes(f.causeStatus))out.push('Record cause as CONFIRMED, LIKELY or UNRESOLVED; do not invent a confirmed cause.');
 if(f.causeStatus==='CONFIRMED'&&!present(f.humanEstablishedCause))out.push('Confirmed cause needs a named human conclusion and supporting evidence.');
 if(f.causeStatus==='LIKELY'&&(!present(f.causeRationale)||!present(f.residualRiskControls)))out.push('A likely cause needs a reason, remaining uncertainty and residual risk controls.');
 if(f.causeStatus==='UNRESOLVED'&&(!present(f.causeRationale)||!present(f.residualRiskControls)))out.push('An unresolved cause needs investigation limits and residual risk controls; confirmed cause is not required.');
 if(!present(f.humanDisposition))out.push('A qualified human disposition rationale is required.');return out;
}
export function qualityIssues(s:State,r:Item,today=new Date().toISOString().slice(0,10)){
 if(r.fields.controlVersion!==2)return ['Historical control format: revise this record to apply the current investigation / effectiveness checklist before a new approval.'];
 const f=r.fields,out:string[]=[];
 if(['quality_events','investigation_records','capa_actions'].includes(r.kind))out.push(...causeIssues(r));
 if(r.kind==='investigation_records'&&(f.eventType==='OOS'||r.sourceIds.some(id=>s.records.find(x=>x.id===id)?.fields.eventType==='OOS'))){
  if(!present(f.phase1Evidence))out.push('OOS phase 1 laboratory investigation evidence is missing.');
  if(!['REQUIRED','NOT_REQUIRED'].includes(f.phase2Decision)||!present(f.phase2Rationale))out.push('Record whether wider phase 2 investigation is required and why.');
  if(f.phase2Decision==='REQUIRED'&&!present(f.phase2Evidence))out.push('Required phase 2 investigation evidence is missing.');
  if(!['NOT_PERFORMED','PERFORMED'].includes(f.retestStatus))out.push('Record whether retesting/resampling was performed.');
  if(f.retestStatus==='PERFORMED'&&(!present(f.retestRationale)||!present(f.originalResultReference)))out.push('Retesting needs an approved rationale and retained original-result reference; no testing into compliance.');
 }
 if(r.kind==='capa_actions'){
  if(!present(f.effectivenessCriterion)||!validDate(f.windowStart)||!validDate(f.windowEnd)||f.windowEnd<f.windowStart)out.push('Define an effectiveness criterion and valid observation start/end dates.');
  if(!f.planReview?.reviewer||!f.planReview?.at||f.planReview.criterion!==f.effectivenessCriterion||f.planReview.windowStart!==f.windowStart||f.planReview.windowEnd!==f.windowEnd)out.push('The exact effectiveness plan needs independent QA approval before implementation.');
  if(!present(f.implementationEvidence)||!present(f.effectivenessEvidence))out.push('Actual implementation and effectiveness evidence are required.');
  if(f.windowEnd>today)out.push('The observation window has not ended; closure stays blocked.');
  if(!validDate(f.observedAt)||f.observedAt<f.windowEnd||f.observedAt>today)out.push('Record a completed effectiveness observation date, after the window and not in the future.');
  if(f.effectivenessOutcome!=='MET')out.push('Effectiveness criterion is not recorded as met; QA must review the actual evidence.');
 }
 return [...new Set(out)];
}
export function reviewCapaPlan(r:Item,reviewer:string,at:string){
 const f=r.fields;if(r.kind!=='capa_actions'||f.createdBy===reviewer)throw Error('An independent QA reviewer must review the CAPA plan.');
 if(f.implementationEvidence||f.effectivenessEvidence)throw Error('Approve the observation plan before recording implementation/effectiveness evidence.');
 if(!present(f.effectivenessCriterion)||!validDate(f.windowStart)||!validDate(f.windowEnd)||f.windowEnd<f.windowStart||f.windowStart<at.slice(0,10))throw Error('A criterion and valid observation window are required.');
 f.planReview={reviewer,at,criterion:f.effectivenessCriterion,windowStart:f.windowStart,windowEnd:f.windowEnd,version:r.version};
}
export function deliverInApp(s:State,actor:string,at:string){let delivered=0,failed=0;for(const n of s.outbox.filter(n=>['PENDING','DELIVERY_FAILED'].includes(n.status)).slice(0,50)){
 n.attempts=(n.attempts||0)+1;const missing=n.targetId&&!s.records.some(r=>r.id===n.targetId);
 if(missing){n.status='DELIVERY_FAILED';n.error='Target record unavailable; inspect notification context.';failed++;}
 else{n.status='DELIVERED_IN_APP';n.channel='WORKSPACE_INBOX';n.deliveredAt=at;n.deliveredTo=actor;delete n.error;delivered++;}
 }return {delivered,failed,channel:'WORKSPACE_INBOX',externalEmailSent:false};}
