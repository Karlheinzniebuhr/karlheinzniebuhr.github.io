---
layout: post
title: "Como censurar al Internet  con reglas simples en RouterOS"
date: 2018-06-10 13:07:35 +0000
categories: [Blog, Technology]
tags: [Technology]
---

Por supuesto estoy muy en contra de la censura. Pero si entendemos como funciona la censura, también nos podemos defender. Así que decidí aprovechar el conocimiento que adquirí sobre RouterOS en la certificación de Mikrotik para tratar de cortarme el servicio de Torrent con un Router Hap Lite.
Como el tráfico de torrent mayormente ya está encriptado, y el bloqueo de puertos no sirve de mucho ya que se puede hacer pasar al tráfico de bittorrent por puertos comunes como el 80, trataremos de prevenir al acceso de las páginas de Torrent.
Hice unas reglas de regex pattern matching en IP > Firewall > Layer 7 Protocols y luego declaré reglas de firewall para hacer drop de los paquetes que coinciden con el patrón de regex declarado. Usé el script que encontré en [esta página](http://gregsowell.com/?p=894) para empezar, voy a ampliarlo más adelante porque esta medio incompleto.

```
# First, we block people from finding torrents 🙂 Using MTKs layer 7 inspection(L7), we match http get requests for bit torrent sites and related sites. Here’s my regex:

/ip firewall layer7-protocol

add comment="" name=torrent-wwws regexp="^.*(get|GET).+(torrent|thepiratebay|isohunt|entertane|demonoid|btjunkie|mininova|flixflux|torrentz|vertor|h33t|btscene|bitunity|bittoxic|thunderbytes|entertane|zoozle|vcdq|bitnova|bitsoup|meganova|fulldls|btbot|flixflux|seedpeer|fenopy|gpirate|commonbits).*\$"

# Now we put in a firewall rule to block with this L7.

/ip firewall filter

add action=drop chain=forward comment="block torrent wwws" disabled=no layer7-protocol=torrent-wwws

# Lets block DNS queries based on the same regex.

/ip firewall layer7-protocol

add comment="" name=torrent-dns regexp="^.+(torrent|thepiratebay|isohunt|entertane|demonoid|btjunkie|mininova|flixflux|torrentz|vertor|h33t|btscene|bitunity|bittoxic|thunderbytes|entertane|zoozle|vcdq|bitnova|bitsoup|meganova|fulldls|btbot|flixflux|seedpeer|fenopy|gpirate|commonbits).*\$"

# Here’s the firewall rule to block:

/ip firewall filter

add action=drop chain=forward comment="block torrent dns" disabled=no dst-port=53 layer7-protocol=torrent-dns protocol=udp
```

Para hacer toda la configuración simplemente hay que copiar y pegar el script de arriba en la terminal de RouterOS.
Las reglas de firewall de RouterOS se ejecutan en secuencia para ahorrar computación, así que si por ejemplo la regla 1 filtra parte del trafico, la regla 2 ya no tiene que procesarlo.
En esta imagen vemos que la regla de bloqueo del DNS se ejecuta cuando trato de acceder a una de las paginas listadas en el regex o si contiene la palabra "torrent".
![](/assets/images/DNS-firewall-rule-1024x516.png)
Si activo la regla que verifica los GET requests, vemos que se ejecuta mucho (hay muchos requests saliendo de la computadora a cada rato) por lo tanto consumira bastante recursos de CPU del router si hay mucho trafico en la red.
![](/assets/images/GET-firewall-rule-1024x485.png)
Al acceder a una página que tiene la palabra torrent en su nombre ya no nos debería cargar.
![](/assets/images/pagina-inaccessible-300x169.png)
Es así de simple, y lo notable es que no necesitas a un servidor para bloquear al tráfico, se puede hacer de forma local y descentralizada en los mismos routers de cada cliente. La tecnología en sí es buena ya que permite a los ISP's detener a ataques de red lo mas cercanamente al origen del ataque sin que afecte a la red de los demás. Pero si se usa para censurar por supuesto que no es bueno. Por lo tanto si notas que no puedes acceder a ciertas páginas, lo primero que recomiendo hacer es hacer un reclamo a tu proveedor de Internet.
Si como clientes dejamos que nos censuren, es probable que lo hagan, pero si reclamamos y nos cambiamos a otro proveedor como última instancia, capaz podamos presionar a las ISP's. Si aún así no te desbloquean, puedes hacer varias cosas, lo más fácil es usar un servicio de VPN que cuesta muy poco, con unos $5-10 por mes ya puedes conseguir uno bueno y usarlo como túnel para tu tráfico de torrent.
