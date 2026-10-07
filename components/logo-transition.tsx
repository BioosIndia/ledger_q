"use client";
import {useEffect,useState} from 'react';
import {Link2} from 'lucide-react';
export function LogoTransition({screen}:{screen:string}){const [show,setShow]=useState(true);useEffect(()=>{setShow(true);const timer=setTimeout(()=>setShow(false),window.matchMedia('(prefers-reduced-motion: reduce)').matches?0:520);return()=>clearTimeout(timer);},[screen]);return show?<div className="logo-transition" aria-hidden="true"><span className="transition-logo"><Link2 size={42}/></span><b>PRAMANEX<span>LEDGER-Q</span></b></div>:null;}
