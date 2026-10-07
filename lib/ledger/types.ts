export const collections=['controlled_sources','requirements','sop_mappings','quality_events','investigation_records','capa_actions','training_impacts','ai_uses','ai_runs','evaluation_runs','dependency_edges','human_decisions','release_passports','audit_events','exports'] as const;
export type Kind=typeof collections[number];
export type Item={id:string;kind:Kind;title:string;status:string;version:number;sourceIds:string[];gaps:string[];owner:string;updated:string;fields:Record<string,any>;hash?:string};
export type State={workspace:{id:string;name:string;synthetic:boolean;productId:string;siteId:string;proofTemplate?:string};records:Item[];jobs:any[];outbox:any[];policy:{provider?:'groq'|'gemini';providerConsent:boolean;model:string;reviewerModel:string;reviewerFallbacks?:string[];visionModel:string;retentionDays:number};corrections:any[];mappings:any[];testCases?:any[]};
export const roles=['Owner','Investigator','QA Reviewer','AI Reviewer','Read Only'] as const;
export const specialists=['Requirement mapping','Deviation / OOS','Change impact','CAPA / effectiveness','AI provenance','AI evaluation','Evidence / audit verifier'];
export const uid=(prefix='LQ')=>prefix+'-'+crypto.randomUUID().slice(0,12);
export const now=()=>new Date().toISOString();
export const newItem=(kind:Kind,title:string,fields:Record<string,any>={},sourceIds:string[]=[],status='REVIEW REQUIRED'):Item=>({id:uid(kind.slice(0,3).toUpperCase()),kind,title,status,version:1,sourceIds,gaps:[],owner:'Unassigned',updated:now(),fields});
