import {spawnSync} from 'node:child_process';
const commands=[["node", "--experimental-strip-types", "--test", "tests/quality-monitor.test.ts"], ["node", "tests/quality-controls.mjs"], ["node", "tests/integration.mjs"], ["node", "tests/extensions.mjs"], ["node", "tests/outcome.test.mjs"], ["node", "--experimental-strip-types", "tests/quality-hosted-runtime.mjs"]];
for(const [cmd,...args] of commands){const r=spawnSync(cmd,args,{stdio:'inherit'});if(r.status!==0)process.exit(r.status||1);}
console.log('Bounded quality checks complete. Professional qualification remains separate.');
