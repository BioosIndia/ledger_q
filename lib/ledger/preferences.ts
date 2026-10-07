/** Device-local display choices cannot configure evidence policy or authority. */
export type Preferences={density:'comfortable'|'compact';accent:'blue'|'cyan';text:'standard'|'large';motion:'system'|'reduced'};
export const defaultPreferences:Preferences={density:'comfortable',accent:'blue',text:'standard',motion:'system'};
export function readPreferences(value:unknown):Preferences{const v=(value&&typeof value==='object'?value:{}) as Record<string,unknown>;return {density:v.density==='compact'?'compact':'comfortable',accent:v.accent==='cyan'?'cyan':'blue',text:v.text==='large'?'large':'standard',motion:v.motion==='reduced'?'reduced':'system'};}
