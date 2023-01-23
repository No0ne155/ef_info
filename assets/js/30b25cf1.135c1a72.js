"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[225],{3905:(e,n,t)=>{t.d(n,{Zo:()=>d,kt:()=>m});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function l(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function o(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var s=r.createContext({}),u=function(e){var n=r.useContext(s),t=n;return e&&(t="function"==typeof e?e(n):l(l({},n),e)),t},d=function(e){var n=u(e.components);return r.createElement(s.Provider,{value:n},e.children)},c={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},p=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,a=e.originalType,s=e.parentName,d=o(e,["components","mdxType","originalType","parentName"]),p=u(t),m=i,h=p["".concat(s,".").concat(m)]||p[m]||c[m]||a;return t?r.createElement(h,l(l({ref:n},d),{},{components:t})):r.createElement(h,l({ref:n},d))}));function m(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var a=t.length,l=new Array(a);l[0]=p;var o={};for(var s in n)hasOwnProperty.call(n,s)&&(o[s]=n[s]);o.originalType=e,o.mdxType="string"==typeof e?e:i,l[1]=o;for(var u=2;u<a;u++)l[u]=t[u];return r.createElement.apply(null,l)}return r.createElement.apply(null,t)}p.displayName="MDXCreateElement"},3579:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>s,contentTitle:()=>l,default:()=>c,frontMatter:()=>a,metadata:()=>o,toc:()=>u});var r=t(7462),i=(t(7294),t(3905));const a={},l="Arbeiten am Numtrip",o={permalink:"/ef_info/2022/12/02/arbeiten-am-numtrip",editUrl:"https://github.com/No0ne155/ef_info/tree/main/blog/2022-12-02-arbeiten-am-numtrip.md",source:"@site/blog/2022-12-02-arbeiten-am-numtrip.md",title:"Arbeiten am Numtrip",description:"Besprechung Benutzereingaben",date:"2022-12-02T00:00:00.000Z",formattedDate:"2. Dezember 2022",tags:[],readingTime:1.52,hasTruncateMarker:!1,authors:[],frontMatter:{},prevItem:{title:"Finaler Blogbeitrag NumTrip",permalink:"/ef_info/2023/01/23/finaler-blogbeitrag-numtrip"},nextItem:{title:"Wiedereinstieg Python",permalink:"/ef_info/2022/08/26/wiedereinstieg-python"}},s={authorsImageUrls:[]},u=[{value:"Besprechung Benutzereingaben",id:"besprechung-benutzereingaben",level:2},{value:"Arbeiten Numtrip",id:"arbeiten-numtrip",level:2},{value:"L\xf6sung wird gesucht!!!",id:"l\xf6sung-wird-gesucht",level:3}],d={toc:u};function c(e){let{components:n,...a}=e;return(0,i.kt)("wrapper",(0,r.Z)({},d,a,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"besprechung-benutzereingaben"},"Besprechung Benutzereingaben"),(0,i.kt)("p",null,"Ich verglich mit Thomas den Code, und wir beide verwenden ein sehr \xe4hnliches system, was die Besprechung kurz hielt."),(0,i.kt)("h2",{id:"arbeiten-numtrip"},"Arbeiten Numtrip"),(0,i.kt)("p",null,"Als erstes habe ich den Auftrag gelesen, und ausgef\xfchrt.\nIch passte das Programm von Wikipedia auf mein Programm an. Der Code sah wie folgt aus:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"def checkandremove(x, y, oldvalue, newvalue):\n    if spielfeld[x][y] == oldvalue:\n        spielfeld[x][y] = newvalue\n        checkandremove(x,y+1,oldvalue,newvalue)\n        checkandremove(x,y-1,oldvalue,newvalue)\n        checkandremove(x+1,y,oldvalue,newvalue)\n        checkandremove(x-1,y,oldvalue,newvalue)\n        game()\n")),(0,i.kt)("p",null,"Nach ein paar tests bemerkte ich, dass wenn z.b. ",(0,i.kt)("inlineCode",{parentName:"p"},"x")," bereits ",(0,i.kt)("inlineCode",{parentName:"p"},"4")," ist, und dann ",(0,i.kt)("inlineCode",{parentName:"p"},"x+1")," \xfcberpr\xfcft wird, dies ausserhalb der liste ist. Deshalb \xe4nderte ich den code zu dem:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"def checkandremove(x, y, oldvalue, newvalue):\n    if spielfeld[x][y] == oldvalue:\n        spielfeld[x][y] = newvalue\n        if y+1 <= 4:\n            checkandremove(x,y+1,oldvalue,newvalue)\n        if y-1 >= 0:\n            checkandremove(x,y-1,oldvalue,newvalue)\n        if x+1 >= 0:\n            checkandremove(x+1,y,oldvalue,newvalue)\n        if x-1 <= 4:\n            checkandremove(x-1,y,oldvalue,newvalue)\n        game()\n")),(0,i.kt)("p",null,"Nach weiteren Tests, fiel mir noch ein gr\xf6sseres noch nicht gel\xf6stes Problem auf."),(0,i.kt)("p",null,(0,i.kt)("img",{src:t(4285).Z,width:"584",height:"529"})),(0,i.kt)("p",null,"Nehmen wir dieses Feld. Wenn nun der Player den input ",(0,i.kt)("inlineCode",{parentName:"p"},"X = 1, Y = 1")," eingibt, kommt dieses Feld heraus:"),(0,i.kt)("p",null,(0,i.kt)("img",{src:t(8359).Z,width:"590",height:"529"})),(0,i.kt)("p",null,"Ich fragte mich warum. Nach dem Betrachten des Codes wusste ich es.\nAuf dieser Darstellung zeige ich es."),(0,i.kt)("p",null,(0,i.kt)("img",{src:t(9016).Z,width:"589",height:"535"})),(0,i.kt)("p",null,"Als erstes wird von ",(0,i.kt)("inlineCode",{parentName:"p"},"1, 1")," aus nach rechts gepr\xfcft. Auf diesem Feld wird dann als n\xe4chstes nach unten gepr\xfcft, und danach nach rechts (wo kein passendes Feld ist), und danach nach links, wo die letzte 4 ist, die entfernt wird. Von diesem Feld aus wird nun in alle richtungen \xfcberpr\xfcft, jedoch keine 4 mehr entdeckt. Die auf dem Bild Blau markierten Pfeile sollten noch gepr\xfcft und entfernt werden, dies passiert jedoch nicht, aufgrund der reihenfolge im code."),(0,i.kt)("p",null,"Ich \xfcberlegte den rest der Zeit noch daran, fand jedoch keine L\xf6sung f\xfcr den Code. Jedoch kann man dieses Beispiel l\xf6sen, indem der Spieler die Position ",(0,i.kt)("inlineCode",{parentName:"p"},"X = 0, Y = 3")," w\xe4hlt."),(0,i.kt)("h3",{id:"l\xf6sung-wird-gesucht"},"L\xf6sung wird gesucht!!!"))}c.isMDXComponent=!0},4285:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/numtrip_problem0-b6318b38293e381cfead0c12709d08b6.png"},8359:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/numtrip_problem1-f823644abc1c31114c4dd076011f5be7.png"},9016:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/numtrip_problem2-857498581d2e084e0e33e5a17c56e943.png"}}]);