"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[148],{3905:(e,n,i)=>{i.d(n,{Zo:()=>o,kt:()=>h});var t=i(7294);function r(e,n,i){return n in e?Object.defineProperty(e,n,{value:i,enumerable:!0,configurable:!0,writable:!0}):e[n]=i,e}function a(e,n){var i=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);n&&(t=t.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),i.push.apply(i,t)}return i}function l(e){for(var n=1;n<arguments.length;n++){var i=null!=arguments[n]?arguments[n]:{};n%2?a(Object(i),!0).forEach((function(n){r(e,n,i[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(i)):a(Object(i)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(i,n))}))}return e}function s(e,n){if(null==e)return{};var i,t,r=function(e,n){if(null==e)return{};var i,t,r={},a=Object.keys(e);for(t=0;t<a.length;t++)i=a[t],n.indexOf(i)>=0||(r[i]=e[i]);return r}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(t=0;t<a.length;t++)i=a[t],n.indexOf(i)>=0||Object.prototype.propertyIsEnumerable.call(e,i)&&(r[i]=e[i])}return r}var d=t.createContext({}),u=function(e){var n=t.useContext(d),i=n;return e&&(i="function"==typeof e?e(n):l(l({},n),e)),i},o=function(e){var n=u(e.components);return t.createElement(d.Provider,{value:n},e.children)},m={inlineCode:"code",wrapper:function(e){var n=e.children;return t.createElement(t.Fragment,{},n)}},p=t.forwardRef((function(e,n){var i=e.components,r=e.mdxType,a=e.originalType,d=e.parentName,o=s(e,["components","mdxType","originalType","parentName"]),p=u(i),h=r,c=p["".concat(d,".").concat(h)]||p[h]||m[h]||a;return i?t.createElement(c,l(l({ref:n},o),{},{components:i})):t.createElement(c,l({ref:n},o))}));function h(e,n){var i=arguments,r=n&&n.mdxType;if("string"==typeof e||r){var a=i.length,l=new Array(a);l[0]=p;var s={};for(var d in n)hasOwnProperty.call(n,d)&&(s[d]=n[d]);s.originalType=e,s.mdxType="string"==typeof e?e:r,l[1]=s;for(var u=2;u<a;u++)l[u]=i[u];return t.createElement.apply(null,l)}return t.createElement.apply(null,i)}p.displayName="MDXCreateElement"},3210:(e,n,i)=>{i.r(n),i.d(n,{assets:()=>d,contentTitle:()=>l,default:()=>m,frontMatter:()=>a,metadata:()=>s,toc:()=>u});var t=i(7462),r=(i(7294),i(3905));const a={},l="Finaler Blogbeitrag NumTrip",s={permalink:"/ef_info/2023/01/23/finaler-blogbeitrag-numtrip",editUrl:"https://github.com/No0ne155/ef_info/tree/main/blog/2023-01-23-finaler-blogbeitrag-numtrip.md",source:"@site/blog/2023-01-23-finaler-blogbeitrag-numtrip.md",title:"Finaler Blogbeitrag NumTrip",description:"Seit der Erstellung des NumTrip.py Games am 16. September 2022 arbeiteten wir immer wieder an diesem NumTrip Spiel. Doch was ist das \xfcberhaupt?",date:"2023-01-23T00:00:00.000Z",formattedDate:"23. Januar 2023",tags:[],readingTime:4.64,hasTruncateMarker:!1,authors:[],frontMatter:{},nextItem:{title:"Arbeiten am Numtrip",permalink:"/ef_info/2022/12/02/arbeiten-am-numtrip"}},d={authorsImageUrls:[]},u=[{value:"Das Spiel",id:"das-spiel",level:2},{value:"Umsetzung",id:"umsetzung",level:2},{value:"Voraussetzungen",id:"voraussetzungen",level:3},{value:"Top-Down Entwurf",id:"top-down-entwurf",level:3},{value:"Konzept Nachbarpr\xfcfung",id:"konzept-nachbarpr\xfcfung",level:3},{value:"Probleme",id:"probleme",level:2},{value:"Tipps:",id:"tipps",level:2},{value:"Fazit",id:"fazit",level:2}],o={toc:u};function m(e){let{components:n,...a}=e;return(0,r.kt)("wrapper",(0,t.Z)({},o,a,{components:n,mdxType:"MDXLayout"}),(0,r.kt)("p",null,"Seit der Erstellung des NumTrip.py Games am 16. September 2022 arbeiteten wir immer wieder an diesem NumTrip Spiel. Doch was ist das \xfcberhaupt?"),(0,r.kt)("h2",{id:"das-spiel"},"Das Spiel"),(0,r.kt)("p",null,"Ziel des Spieles ",(0,r.kt)("em",{parentName:"p"},"NumTrip")," ist es, ein Feld mit dem Wert 128 (oder eine andere selbst festgelegte Zweierpotenz) zu erreichen. Zum Beginn hat man nur ein Feld mit zuf\xe4lligen Zweierpotenzen. Indem man Koordinaten des Feldes aussucht, das Nachbarfelder mit dem gleichen Wert hat, kann man den Wert dieses Feldes verdoppeln, und die umliegenden Felder verschwinden lassen. Nun generieren oben am Feld neue Zahlen. So kann man versuchen, die Felder so lange zu kombinieren, bis man 128 erreicht hat. So ",(0,r.kt)("strong",{parentName:"p"},"gewinnt")," man das Spiel."),(0,r.kt)("p",null,"Jedoch kann man auch verlieren. Wenn es keine Felder mehr gibt, die man kombinieren kann, hat man ",(0,r.kt)("strong",{parentName:"p"},"verloren"),"."),(0,r.kt)("h2",{id:"umsetzung"},"Umsetzung"),(0,r.kt)("h3",{id:"voraussetzungen"},"Voraussetzungen"),(0,r.kt)("p",null,"Um meine Version des NumTrip zu spielen, braucht man eine Applikation (z.b. VisualStudioCode) um ein Python Programm laufen zu lassen. Unsere verwendete Python Version ist ",(0,r.kt)("em",{parentName:"p"},"Python 3.10.6"),". Meinen Code findet man auf ",(0,r.kt)("a",{parentName:"p",href:"https://github.com/No0ne155/ef_info/blob/main/NumTrip/NumTrip_FINAL.py"},"GitHub")," Diesen kann man in ein Dokument in VSCode kopieren, dass die Endung ",(0,r.kt)("inlineCode",{parentName:"p"},".py")," hat. Damit definiert man, dass es ein Python Dokument ist. "),(0,r.kt)("h3",{id:"top-down-entwurf"},"Top-Down Entwurf"),(0,r.kt)("p",null,"Um ein grosses Projekt besser erf\xfcllen zu k\xf6nnen, verwendet man einen sogenannten Top-Down Entwurf. Mein Top-Down Entwurf hat auf der obersten Ebene das NumTrip-Game. Dies teilt man nun in immer kleinere Teilprobleme auf, bis man viele kleine Dinge hat, die einfacher sind. Diese f\xfcgt man dann zusammen, damit man ein komplettes Projekt hat.\n",(0,r.kt)("img",{src:i(618).Z,width:"1716",height:"801"}),"\nz.b. im Bereich Feld, habe ich f\xfcr das Generieren des Feldes die Funktion ",(0,r.kt)("inlineCode",{parentName:"p"},"generatefield()")," erstellt. Diese Funktion generiert zufallszahlen, und f\xfcgt die in die ",(0,r.kt)("inlineCode",{parentName:"p"},"spielfeld")," Liste. F\xfcr das Ausgeben des Feldes habe ich die Funktion ",(0,r.kt)("inlineCode",{parentName:"p"},"printfield()")," erstellt. Diese Druckt das Design des Spielfeldes, und entsprechend der Gr\xf6sse der Zahl, wird die Funktion so angepasst, dass das Design nicht durcheinander kommt. Diese beiden Funktionen zusammen ergeben das Spielfeld. Zum Schluss werden die Funktionen an der richtigen Stelle im Code oder in anderen Funktionen aufgerufen. So \xe4hnlich funktioniert es auch mit allen anderen Teilbereichen die im Top-Down Entwurf geschrieben sind."),(0,r.kt)("h3",{id:"konzept-nachbarpr\xfcfung"},"Konzept Nachbarpr\xfcfung"),(0,r.kt)("p",null,"Im Spiel verwende ich viele sogenannte Algorithmen. Einer davon wird z.b. f\xfcr die \xdcberpr\xfcfung ob eine Nachbarzelle vorhanden ist eingesetzt. Die Funktion wird ben\xf6tigt, denn wir wollen die Zahl ja nur verdoppeln, wenn sie auch mindestens ein Feld rundherum hat, dass den gleichen Wert hat. Daf\xfcr erstellen wir die folgende Funktion: ",(0,r.kt)("inlineCode",{parentName:"p"},"validateneighbour(y, x)")," Dabei sind ",(0,r.kt)("inlineCode",{parentName:"p"},"y")," und ",(0,r.kt)("inlineCode",{parentName:"p"},"x")," Parameter die man beim Aufrufen der Funktion mitgibt. In diesem Fall entsprechen die Parameter den Koordinaten im Spielfeld. Die Parameter sind in der gew\xe4hlten Reihenfolge, da ",(0,r.kt)("inlineCode",{parentName:"p"},"y")," f\xfcr die Zeile steht, und ",(0,r.kt)("inlineCode",{parentName:"p"},"x")," f\xfcr die Spalte."),(0,r.kt)("p",null,"Beim Aufrufen der Funktion wird \xfcberpr\xfcft, ob die Funktion ",(0,r.kt)("inlineCode",{parentName:"p"},"True")," zur\xfcckgibt. Nun muss die Funktion ",(0,r.kt)("inlineCode",{parentName:"p"},"True")," zur\xfcckgeben, wenn ein Nachbar vorhanden ist, sonst muss ",(0,r.kt)("inlineCode",{parentName:"p"},"False")," zur\xfcckgegeben werden. Im ersten Schritt pr\xfcfen wir ob in die ",(0,r.kt)("inlineCode",{parentName:"p"},"x-1")," Richtung ein Nachbar ist. Damit kein List-Index ERROR erscheint, pr\xfcfen wir, ob die Zahl gr\xf6sser als ",(0,r.kt)("inlineCode",{parentName:"p"},"1")," ist, da wir ",(0,r.kt)("inlineCode",{parentName:"p"},"1")," subtrahieren, und nicht ins Negative wollen. Diese \xdcberpr\xfcfung findet mit "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-py"},"if x >= 1:\n")),(0,r.kt)("p",null,"statt. Wenn dieses Statement zutrifft, geht es weiter zur \xdcberpr\xfcfung, ob die ausgew\xe4hlten Koordinaten den gleichen Wert gespeichert haben, wie die selbe Koordinate aber mit ",(0,r.kt)("inlineCode",{parentName:"p"},"x-1"),". "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-py"},"if spielfeld[x-1][y] == spielfeld[x][y]:\n            return True   \n")),(0,r.kt)("p",null,"Dies wird nun in alle anderen Richtungen genau gleich angewendet. Nat\xfcrlich mit anderen werten.\nWenn nie ein Feld den gleichen Wert hat, wird zum Schluss ",(0,r.kt)("inlineCode",{parentName:"p"},"False")," zur\xfcckgegeben. Gesamt sieht der Algorithmus dann so aus:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-py"},"def validateneighbour(y,x):\n    if x >= 1: \n        if spielfeld[x-1][y] == spielfeld[x][y]: \n            return True                          \n    if x <= 3:\n        if spielfeld[x+1][y] == spielfeld[x][y]:\n            return True\n    if y >= 1:\n        if spielfeld[x][y-1] == spielfeld[x][y]:\n            return True\n    if y <= 3:\n        if spielfeld[x][y+1] == spielfeld[x][y]:\n            return True\n    return False\n")),(0,r.kt)("h2",{id:"probleme"},"Probleme"),(0,r.kt)("p",null,"Mein gr\xf6sstes Problem war, dass ich gewisse Funktionen so aufbaute, dass sie Funktionierten, aber nicht mit k\xfcnftigen Funktionen kompatibel waren. So kam ich oft an den Punkt, dass ich vieles \xfcberarbeiten musste, da ich fr\xfcher nicht gut genug arbeitete."),(0,r.kt)("p",null,"Es kam sogar so weit, dass ich Fehler hatte, nicht wusste woher, die Logik keinen Sinn mehr ergab, so dass ich mich entschied, von vorne anzufangen. Ich verwendete nat\xfcrlich gewisse Funktionen wieder, aber ich fing wieder von 0 an, damit ich alles nochmals Schritt f\xfcr Schritt durchgehen kann. Z.b. f\xfcgte ich in der ",(0,r.kt)("inlineCode",{parentName:"p"},"printfield()")," Funktion die neuen, angepassten Strings (der Zahlenwert mit passender Anzahl Leerzeichen) HINTEN an die Liste, l\xf6schte sie jedoch nie, weshalb sich mein Spielfeld nicht Ver\xe4nderte, egal was ich als Input gab. Solche kleinen Fehler w\xe4ren mir sonst nicht aufgefallen."),(0,r.kt)("h2",{id:"tipps"},"Tipps:"),(0,r.kt)("p",null,"Wenn du auch so ein Programm schreibst, \xfcberleg dir manchmal zuerst, was du sp\xe4ter auch noch in die Funktion einf\xfcgen musst, damit du sie sp\xe4ter nicht nochmals schreiben musst. "),(0,r.kt)("p",null,"Ebenfalls ist es hilfreich, wenn du deinen Funktionen und Variablen Namen gibst, die dir klar machen, was sie tun, sodass du den \xdcberblick behaltest. Aber mach die Namen auch nicht zu lange, denn es kann sehr m\xfchsam sein, den Namen ",(0,r.kt)("inlineCode",{parentName:"p"},"spielfeldnice[playerinputY][playerinputX]")," in einer Funktion 4 mal zu schreiben."),(0,r.kt)("h2",{id:"fazit"},"Fazit"),(0,r.kt)("p",null,"Mit mehr Zeit, w\xe4ren noch viele Features mehr m\xf6glich gewesen. Da man aber nicht immer viel Zeit hat, sich die Zeit nicht nimmt, oder ein Problem hat, dass sich einfach nicht l\xf6sen will, bin ich ganz zufrieden mit meinem Resultat. Am Anfang stockte es, doch als ich im Neugeschriebenen Programm (fast) alle Probleme gefunden hatte, ging alles sehr schnell. Weitere Features zu implementieren w\xe4ren nicht die Komplizierteste Sache, jedoch muss man es machen, und nicht nur dar\xfcber Nachdenken"),(0,r.kt)("p",null,"Allem in allem war es ein Gro\xdfartiges Projekt."))}m.isMDXComponent=!0},618:(e,n,i)=>{i.d(n,{Z:()=>t});const t=i.p+"assets/images/topdown-5792a9fb09895f79f25d13d161db8560.png"}}]);