"use client";
import {useRef,useState} from 'react';
import styles from './media-guide.module.css';
type Lang='en'|'hi';
export default function MediaGuide({product,slug,caseHref,checklistHref}:{product:string;slug:string;caseHref:string;checklistHref?:string}){
 const [language,setLanguage]=useState<Lang>('en'),[failed,setFailed]=useState(false);
 const video=useRef<HTMLVideoElement>(null);const pending=useRef({time:0,resume:false});
 function change(value:Lang){if(value===language)return;pending.current={time:video.current?.currentTime||0,resume:!!video.current&&!video.current.paused};video.current?.pause();setFailed(false);setLanguage(value);}
 return <section className={styles.guide} id="video-demo" aria-labelledby={`${slug}-video-title`}>
 <div className={styles.heading}><div><span className={styles.kicker}>TWO-MINUTE GUIDED WORK SAMPLE</span><h2 id={`${slug}-video-title`}>{product}: follow the evidence.</h2><p>Choose English or Hindi narration. Inspect the saved synthetic case after the guide.</p></div><label className={styles.language}>Narration language<select value={language} onChange={e=>change(e.target.value as Lang)}><option value="en">English</option><option value="hi">हिन्दी / Hindi</option></select></label></div>
 <video key={language} ref={video} controls playsInline preload="metadata" poster={`/videos/${slug}-poster.webp`} aria-label={`${product} two-minute ${language==='en'?'English':'Hindi'} narrated synthetic workflow guide`} onError={()=>setFailed(true)} onLoadedMetadata={()=>{const v=video.current;if(!v)return;v.currentTime=Math.min(pending.current.time,Math.max(0,v.duration-.1));if(pending.current.resume)v.play().catch(()=>{});}}>
 <source src={`/videos/${slug}-walkthrough-${language}.mp4`} type="video/mp4"/><track kind="captions" src={`/videos/${slug}-walkthrough-${language}.vtt`} srcLang={language} label={language==='en'?'English':'Hindi'} default/>Your browser cannot play this video. Use the download or transcript below.
 </video>
 {failed&&<p role="alert">The video could not load. Download the guide or read its transcript below; the workspace has not changed.</p>}
 <p className={styles.boundary}>Animated explanation of the saved synthetic fixture, not a live screen recording or a latency/accuracy benchmark. Human review remains required.</p>
 <div className={styles.actions}><a href={caseHref}>Open the saved working case →</a><a href={`/videos/${slug}-walkthrough-${language}.mp4`} download>Download {language==='en'?'English':'Hindi'} video</a><a href={`/videos/${slug}-transcript-${language}.txt`}>Read transcript</a>{checklistHref&&<a href={checklistHref} target="_blank" rel="noopener noreferrer">Ten-step checklist PDF ↗</a>}</div>
 </section>;
}
