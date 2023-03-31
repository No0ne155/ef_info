# Netzwerke

Zusammenfassung zu den Punkten der Kapitel 3 - 8

## Switch

Ein Switch ist ein Gerät, welches im lokalen Netzwerk weiss, welcher Host wo ist, und ein Paket nur an den Richtigen Host weiterleitet, und nicht an alle eine Kopie sendet. 

![](img/switch.png)

Wie im Bild gezeigt, sendet der Switch ein Paket nur von Grün zu grün.

## IP-Adresse

Die IP-Adresse ist die Individuelle Adresse jedes Hostes in einem Netzwerk (Auch das Internet ist ein Netzwerk). Sie ist schichtartig aufgebaut, dass alle im gleichen Netzwerk eine ähnliche IP haben.
![](img/ip.png)

Dieses Netzwerk hat z.b. generell die IP `10.x.x.x`. Der Standort New York hat nun den zusatz `10.20.x.x` und das Marketing Team den zusatz `10.20.77.x` wobei x immer den individuellen Host beschreibt. Die anderen standorte unterscheiden sich nun nur im 2. Octett der Binären IP.

## Router

Der Router ist ein Gerät, welches Netzwerke untereinander verbindet. Das Internet ist dann im Grossen und Ganzen eine Verbindung von sehr vielen Routern die dich weiterleiten bis du am richtigen Ort bist.

![](img/router.png)

Wie im Bild dargestellt verbinden sich die Switches eines Netzwerk mit dem Router, der die Netzwerke untereinander verbindet, jedoch auch mit dem Internet verbindet.

### Router Tabelle

Die Router Tabelle besteht aus allen Netzwerken die eine Router kennt, und mit jeder anfrage zu einem Neuen Server wird diese Tabelle grösser. So lernt der Router immer mehr, und "Lernt".

## MAC-Adresse

Die MAC - Adresse (Media-Access-Control-Adress) ist die Individuelle Adresse eines NIC (Network Interface Card). NIC ermöglicht Kommunikation mit der Physischen schicht, weshalb dort die Individuelle Adresse ist. Denn die IP bezieht sich auf das Netzwerk, und kann sich je nach Netzwerk ändern.

![](img/mac.png)

MAC-Adressen bestehen aus 48 Bits, die als 12 Hexadezimale zeichen angegeben werden. Die MAC-Adresse ist die Individuelle, unverwechselbare Adresse eines Gerätes mit Internetzugang.

### MAC-Tabelle

Die MAC-Tabelle beinhaltet alle MAC-Adressen die ein Gerät mit NIC kennt. Dies beinhaltet auch die MAC-Adressen von Routern und Switches.

## ARP

ARP (Adress-Resolution-Protocol) wird verwendet, um die IP-Adresse mit der MAC-Adresse zu verknüpfen.

### ARP ohne Router
ARP-Request wird verwendet, wenn der Host die Ziel-IP-Adresse kennt, aber die MAC-Adresse der IP nicht kennt.

![](img/arp2.png)

Der Host sendet nun einen ARP-Request an die IP des Servers, mit der MAC-Adresse ffff.ffff.ffff, da diese für diesen fall reserviert ist. Im ARP-Request ist die MAC-Adresse und IP des Hostes enthalten, damit der Ziel-Server problemlos antworten kann. 

Der Ziel-Server antwortet nun mit seiner IP und MAC-Adresse, und fügt die IP und MAC-Adresse seinem ARP-Cache zu.

![](img/arp3.png)

Sobald diese Nachricht beim Host ankam, kann er seinen Layer-2 Header mit der MAC-Adresse ergänzen, und seine Nachricht schicken. Von nun an, ist die IP mit der MAC-Adresse bei beiden im ARP-Cache gespeichert, und dieser Schritt kann übersprungen werden.

### ARP mit Router

(:
### Noch zu bearbeitende Punkte:

Gateway

Ethernet-Frame