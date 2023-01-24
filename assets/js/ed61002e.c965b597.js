"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[54],{3905:(e,t,n)=>{n.d(t,{Zo:()=>m,kt:()=>s});var r=n(7294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function l(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function p(e,t){if(null==e)return{};var n,r,i=function(e,t){if(null==e)return{};var n,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var u=r.createContext({}),o=function(e){var t=r.useContext(u),n=t;return e&&(n="function"==typeof e?e(t):l(l({},t),e)),n},m=function(e){var t=o(e.components);return r.createElement(u.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},c=r.forwardRef((function(e,t){var n=e.components,i=e.mdxType,a=e.originalType,u=e.parentName,m=p(e,["components","mdxType","originalType","parentName"]),c=o(n),s=i,f=c["".concat(u,".").concat(s)]||c[s]||d[s]||a;return n?r.createElement(f,l(l({ref:t},m),{},{components:n})):r.createElement(f,l({ref:t},m))}));function s(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var a=n.length,l=new Array(a);l[0]=c;var p={};for(var u in t)hasOwnProperty.call(t,u)&&(p[u]=t[u]);p.originalType=e,p.mdxType="string"==typeof e?e:i,l[1]=p;for(var o=2;o<a;o++)l[o]=n[o];return r.createElement.apply(null,l)}return r.createElement.apply(null,n)}c.displayName="MDXCreateElement"},3016:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>u,contentTitle:()=>l,default:()=>d,frontMatter:()=>a,metadata:()=>p,toc:()=>o});var r=n(7462),i=(n(7294),n(3905));const a={},l="NumTrip Top Down Entwurf",p={unversionedId:"numTrip/Top-Down_Entwurf_Numtrip",id:"numTrip/Top-Down_Entwurf_Numtrip",title:"NumTrip Top Down Entwurf",description:"Top-Down Entwurf:",source:"@site/docs/numTrip/Top-Down_Entwurf_Numtrip.md",sourceDirName:"numTrip",slug:"/numTrip/Top-Down_Entwurf_Numtrip",permalink:"/ef_info/docs/numTrip/Top-Down_Entwurf_Numtrip",draft:!1,editUrl:"https://github.com/No0ne155/ef_info/tree/main/docs/numTrip/Top-Down_Entwurf_Numtrip.md",tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"NumTrip Listenstruktur",permalink:"/ef_info/docs/numTrip/Datenstruktur"},next:{title:"Listen 2D Referenzen",permalink:"/ef_info/docs/python/referenzen"}},u={},o=[{value:"Top-Down Entwurf:",id:"top-down-entwurf",level:2}],m={toc:o};function d(e){let{components:t,...a}=e;return(0,i.kt)("wrapper",(0,r.Z)({},m,a,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"numtrip-top-down-entwurf"},"NumTrip Top Down Entwurf"),(0,i.kt)("h2",{id:"top-down-entwurf"},"Top-Down Entwurf:"),(0,i.kt)("p",null,(0,i.kt)("img",{src:n(918).Z,width:"1716",height:"801"})),(0,i.kt)("p",null,"Der Top-Down Entwurf hat auf der Obersten Ebene das NumTrip-Game. Dies teilt man nun in immer kleinere Teilprobleme auf, bis man viele kleine dinge hat, die einfacher sind. Diese f\xfcgt man dann zusammen, damit man ein komplettes Projekt hat. F\xfcr das NumTrip spiel konnte ich es so unterteilen: "),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h2",{parentName:"li",id:"feld"},"Feld"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h3",{parentName:"li",id:"generieren"},"Generieren"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Random Zahlen verwenden"))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h3",{parentName:"li",id:"ausgeben"},"Ausgeben"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Feld in sch\xf6nem Layout mit Zahlen aus Liste ausgeben"))))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h2",{parentName:"li",id:"ende"},"Ende"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h3",{parentName:"li",id:"gewinnen"},"Gewinnen"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Ein Feld hat den im code gesetzten endwert erreicht"),(0,i.kt)("li",{parentName:"ul"},"Spiel beenden, Gewinnnachricht anzeigen, Feld nochmals anzeigen"))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h3",{parentName:"li",id:"verlieren"},"Verlieren"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Keine m\xf6glichkeit mehr ein Feld zu w\xe4hlen"),(0,i.kt)("li",{parentName:"ul"},"Endnachricht anzeigen, Feld nochmals Anzeigen, Spiel beenden"))))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h2",{parentName:"li",id:"spielerinteraktion"},"Spielerinteraktion"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h3",{parentName:"li",id:"erfragen"},"Erfragen"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Solange bis der Input als Valide best\xe4tigt wurde"))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h3",{parentName:"li",id:"validieren"},"Validieren"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Ist der Input eine Zahl?"),(0,i.kt)("li",{parentName:"ul"},"Ist der Input im Spielfeld?"))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("h3",{parentName:"li",id:"reagieren"},"Reagieren"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Die umliegenden Felder mit der gleichen Zahl entfernen"),(0,i.kt)("li",{parentName:"ul"},"Das ausgew\xe4hlte Feld Verdoppeln"),(0,i.kt)("li",{parentName:"ul"},"Die Felder oberhalb der Nachbarfelder nach unten bewegen")))))))}d.isMDXComponent=!0},918:(e,t,n)=>{n.d(t,{Z:()=>r});const r=n.p+"assets/images/topdown_new-5792a9fb09895f79f25d13d161db8560.png"}}]);