"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[977],{3905:(e,n,t)=>{t.d(n,{Zo:()=>f,kt:()=>d});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function o(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function a(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?o(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):o(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function c(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},o=Object.keys(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var p=r.createContext({}),l=function(e){var n=r.useContext(p),t=n;return e&&(t="function"==typeof e?e(n):a(a({},n),e)),t},f=function(e){var n=l(e.components);return r.createElement(p.Provider,{value:n},e.children)},s={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},u=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,o=e.originalType,p=e.parentName,f=c(e,["components","mdxType","originalType","parentName"]),u=l(t),d=i,m=u["".concat(p,".").concat(d)]||u[d]||s[d]||o;return t?r.createElement(m,a(a({ref:n},f),{},{components:t})):r.createElement(m,a({ref:n},f))}));function d(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var o=t.length,a=new Array(o);a[0]=u;var c={};for(var p in n)hasOwnProperty.call(n,p)&&(c[p]=n[p]);c.originalType=e,c.mdxType="string"==typeof e?e:i,a[1]=c;for(var l=2;l<o;l++)a[l]=t[l];return r.createElement.apply(null,a)}return r.createElement.apply(null,t)}u.displayName="MDXCreateElement"},5377:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>p,contentTitle:()=>a,default:()=>s,frontMatter:()=>o,metadata:()=>c,toc:()=>l});var r=t(7462),i=(t(7294),t(3905));const o={},a="Listen 2D Referenzen",c={unversionedId:"python/referenzen",id:"python/referenzen",title:"Listen 2D Referenzen",description:"Die Listen sind eigentlich die selben, jedoch mit anderem Namen. So ver\xe4ndert sich beim \xe4ndern der einen Liste auch die andere.",source:"@site/docs/python/referenzen.md",sourceDirName:"python",slug:"/python/referenzen",permalink:"/ef_info/docs/python/referenzen",draft:!1,editUrl:"https://github.com/No0ne155/ef_info/tree/main/docs/python/referenzen.md",tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"NumTrip Top Down Entwurf",permalink:"/ef_info/docs/numTrip/Top-Down_Entwurf_Numtrip"}},p={},l=[],f={toc:l};function s(e){let{components:n,...t}=e;return(0,i.kt)("wrapper",(0,r.Z)({},f,t,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"listen-2d-referenzen"},"Listen 2D Referenzen"),(0,i.kt)("p",null,"Die Listen sind eigentlich die selben, jedoch mit anderem Namen. So ver\xe4ndert sich beim \xe4ndern der einen Liste auch die andere."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"matrix = []\n\nzeile = [0, 1, 0]\nfor i in range(3):\n    matrix.append(zeile)\n\nprint(matrix)\n\nmatrix[1][1] = 0 # setzt Wert in Zeile 1 in der Mitte auf 0 Setzen\n\nprint(matrix)\n")))}s.isMDXComponent=!0}}]);