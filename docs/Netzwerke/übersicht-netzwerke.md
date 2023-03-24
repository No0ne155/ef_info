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

### Noch zu bearbeitende Punkte:

MAC-Adresse

Gateway

Mac-Tabelle

Ethernet-Frame

ARP