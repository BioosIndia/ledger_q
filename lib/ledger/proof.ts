import type {State} from './types';
import {emptyWorkspace,find,extract,assertDecision,invalidate,evidenceGaps,validateCandidate,evaluationPack} from './engine';
export type ProofStep={id:string;title:string;status:'DEMONSTRATED'|'PARTIAL'|'NOT ESTABLISHED';observation:string;href:string};
/** Reads the saved public fixture. Simulations use isolated copies; no public or private record is edited. */
export function tenStepProof(s:State,revision:number,originals:{id:string;verified:boolean}[]){
 if(s.workspace.id!=='LQ-PUBLIC'||!s.workspace.synthetic)throw new Error('Checklist is restricted to the saved public synthetic proof.');
 const fresh=emptyWorkspace('CHECK-EMPTY');const lab=find(s,'SRC-LAB-026'),sop=find(s,'SRC-SOP-014'),event=find(s,'EVT-OOS-026');
 const requirements=extract(s,sop);let denied=false;try{assertDecision(s,event,'APPROVED');}catch{denied=true;}
 const changed=structuredClone(s);const affected=invalidate(changed,sop.id);const stale=find(changed,event.id).status==='STALE';
 const checks=evaluationPack();const provider=s.records.find(r=>r.kind==='ai_uses'&&r.id==='AI-QA-01');
 const grounded=validateCandidate(s,{facts:[{sourceId:lab.id,version:lab.version,span:lab.fields.text,statement:lab.fields.text}]});
 const unsupported=validateCandidate(s,{facts:[{sourceId:lab.id,version:lab.version,span:'Root cause confirmed.',statement:'Root cause confirmed.'}],approval:true});
 const step=(id:string,title:string,pass:boolean,observation:string,href:string):ProofStep=>({id,title,status:pass?'DEMONSTRATED':'PARTIAL',observation,href});
 const steps:ProofStep[]=[
 step('01','Start from an empty workspace',fresh.records.length===0&&fresh.jobs.length===0,'The empty-workspace control has zero records and jobs. Sign-in creates or reuses empty private work; public proof is selected separately.','/app'),
 step('02','Keep the original evidence',originals.length>0&&originals.every(x=>x.verified),`${originals.filter(x=>x.verified).length}/${originals.length} saved public source originals match their recorded SHA-256. This is synthetic evidence, not company data.`,'/sources?demo=1'),
 step('03','Link requirements to exact text',requirements.length>0&&requirements.every(r=>r.fields.sourceVersion===sop.version&&r.fields.sourceHash===sop.hash),`${requirements.length} exact-text requirements can be reproduced from ${sop.id}, revision ${sop.version}. Applicability still requires review.`,'/requirements?demo=1'),
 step('04','Show the conflict without guessing',event.status==='HOLD'&&lab.fields.values?.length===2&&evidenceGaps(s,event).length>0,'94.2% and 99.1% remain distinct for the same batch and method. Root cause and disposition are not established.','/events?demo=1'),
 step('05','Bound the candidate output',grounded.valid&&!unsupported.valid,'An exact source-backed candidate passes the grounding check. An unsupported root-cause statement and agent approval attempt are rejected.','/ai-evaluation?demo=1'),
 step('06','Stop unsupported approval',denied,'Approval of the unresolved quality event is blocked by the actual decision guard. The public proof contains no real QA sign-off.','/review?demo=1'),
 step('07','Recheck when evidence changes',affected.length>0&&stale,`An isolated source-change simulation marks ${affected.length} dependent records stale or suspended. The original saved public proof is unchanged.`,'/changes?demo=1'),
 step('08','Expose repeatable checks',checks.every(c=>c.pass),`${checks.filter(c=>c.pass).length}/${checks.length} deterministic synthetic control fixtures pass. This count is not model accuracy, professional validation or release permission.`,'/ai-evaluation?demo=1'),
 {id:'09',title:'Measure real professional benefit',status:'NOT ESTABLISHED',observation:'No real-user time savings, correction reduction or accuracy percentage is established. A supervised pilot with a manual baseline and qualified QA review is required.',href:'/work-samples/LEDGER_Q_Ten_Step_Checklist.pdf'},
 {id:'10',title:'Qualify live use and operations',status:'PARTIAL',observation:`The saved proof keeps ${provider?.id||'AI intended use'} ${provider?.status||'unqualified'}. Live model connection receipts are separate from quality qualification. Security, backup recovery and professional intended-use acceptance need their own evidence.`,href:'/ai-registry?demo=1'},
 ];
 return {product:'LEDGER-Q',workspaceId:s.workspace.id,revision,scope:'Saved synthetic proof plus isolated engineering control checks. Not independent validation, batch release or a commercial quality assessment.',checkedAt:new Date().toISOString(),steps,checks,originals,realUserBenefitsEstablished:false};
}
