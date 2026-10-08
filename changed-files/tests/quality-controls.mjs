import assert from 'node:assert/strict';
import fs from 'node:fs';
import ts from 'typescript';
fs.mkdirSync('.test-build',{recursive:true});for(const name of ['types','quality-controls'])fs.writeFileSync('.test-build/'+name+'.js',ts.transpileModule(fs.readFileSync('lib/ledger/'+name+'.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText.replace(/from '(\.\/[^']+)'/g,"from '$1.js'"));
const {qualityIssues,causeIssues,reviewCapaPlan,deliverInApp}=await import('../.test-build/quality-controls.js');
const s={records:[],outbox:[]},record={id:'capa',kind:'capa_actions',version:1,sourceIds:[],fields:{controlVersion:2,createdBy:'author',causeStatus:'UNRESOLVED',causeRationale:'Investigation did not establish a confirmed cause.',residualRiskControls:'Preserve affected evidence and restrict use.',humanDisposition:'QA retains hold pending specific evidence.',effectivenessCriterion:'No recurrence in the agreed window.',windowStart:'2026-10-09',windowEnd:'2026-10-12'}};let n=0;
function check(name,fn){fn();n++;console.log('PASS '+name);}
check('Unresolved cause remains honest with qualified human rationale',()=>assert.equal(causeIssues(record).length,0));
check('Unknown cause without residual controls blocks progression',()=>assert(causeIssues({...record,fields:{...record.fields,residualRiskControls:''}}).length));
check('CAPA author cannot approve own plan',()=>assert.throws(()=>reviewCapaPlan(structuredClone(record),'author','2026-10-08T10:00:00Z')));
check('Plan cannot be retrospectively approved after implementation evidence',()=>assert.throws(()=>reviewCapaPlan({...record,fields:{...record.fields,implementationEvidence:'Implemented'}},'qa','2026-10-08T10:00:00Z')));
reviewCapaPlan(record,'qa','2026-10-08T10:00:00Z');record.fields.implementationEvidence='Authorized implementation record';record.fields.effectivenessEvidence='Observed recurrence log';record.fields.observedAt='2026-10-12';record.fields.effectivenessOutcome='MET';
check('Observation window blocks premature closure',()=>assert(qualityIssues(s,record,'2026-10-10').some(x=>/window/.test(x))));
check('Completed window with reviewed plan and actual evidence is reviewable',()=>assert.equal(qualityIssues(s,record,'2026-10-13').length,0));
check('Changing effectiveness criterion invalidates plan review',()=>assert(qualityIssues(s,{...record,fields:{...record.fields,effectivenessCriterion:'Changed criterion'}},'2026-10-13').length));
check('OOS investigation requires phase 1, phase 2 rationale and retest status',()=>assert(qualityIssues(s,{...record,kind:'investigation_records',fields:{...record.fields,eventType:'OOS'}},'2026-10-13').length>=3));
check('Failed inbox delivery stays visible and can be retried',()=>{const x={records:[],outbox:[{id:'1',status:'PENDING',targetId:'missing'}]};assert.equal(deliverInApp(x,'member','2026-10-08').failed,1);assert.equal(x.outbox[0].status,'DELIVERY_FAILED');x.records.push({id:'missing'});assert.equal(deliverInApp(x,'member','2026-10-08').delivered,1);assert.equal(x.outbox[0].channel,'WORKSPACE_INBOX');assert.equal(x.outbox[0].attempts,2);});
check('Inbox delivery never claims an email was sent',()=>assert.equal(deliverInApp({records:[],outbox:[{id:'notice',status:'PENDING'}]},'member','2026-10-08').externalEmailSent,false));
console.log(JSON.stringify({passed:n,failed:0,scope:'Synthetic quality gates and in-app delivery; not professional qualification.'}));
