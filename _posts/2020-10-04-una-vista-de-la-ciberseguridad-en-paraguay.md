---
layout: post
title: "Una vista de la Ciberseguridad en Paraguay"
date: 2020-10-04 17:49:58 +0000
categories: ["Tech", "Blog-es"]
---

## Introducción

En este post contaré cómo me preparé, y lo que encontré en el camino de mi preparación para el tema del panel del evento HackdayPY.

Todo empezó cuando Victor Cáceres me preguntó si quería formar parte del panel de HackdayPY para hablar brevemente al respecto de la Ciberseguridad del Paraguay. Primero pensé, bueno en realidad mi ámbito actual de trabajo no es específicamente el de la ciberseguridad. Luego me acordé de que hace años me encargo de seguridad de redes en una ISP. También la seguridad informática siempre fue mi hobby y tal vez hasta un talento no tan explotado.

Además, Victor acordó que para mucha gente podría ser interesante mi trabajo con los datos abiertos. Pensándolo bien, combinar mi experiencia y gusto en el análisis de datos, con mi interés por la seguridad informática, podría ser divertido para mí y potencialmente interesante para los demás. Así fue como acepté al desafió.

---

## Colección de datos

El tema del panel es: "Un punto de vista real sobre la Ciberseguridad en Paraguay". Un análisis suelo empezar con datos. Primero tenía que obtener datos cibernéticos del país. Ya había hecho [escaneos masivos con Nmap](https://www.karlbooklover.com/comprobando-15m-ips-paraguayas-por-cve-2018-14847/) en el pasado. Como me gusta mucho nmap, mi primer idea fue hacer lo mismo, pero existe una herramienta aún más fácil y rápida de usar, Shodan. [Shodan](https://www.shodan.io/) es un buscador de dispositivos conectados al Internet, también llamado Internet of Things o IoT. En síntesis lo que hace es escanear toda la Internet pública y almacena los datos encontrados en una base de datos.

### Shodan o Nmap para la exploración del Internet ?

Con ayuda de una base de datos es fácil hacer peticiones de forma rápida o generar estadísticas interesantes. El punto fuerte de shodan en comparación a nmap es que usa menos recursos y tiempo. Con nmap los escaneos son activos, es decir uno debe utilizar su propio ancho de banda y tiempo de cpu para comprobar cada IP pública, lo cual conlleva mucho trabajo. Si bien ya hay herramientas como [Zmap](https://github.com/zmap/zmap) y [Masscan](https://github.com/robertdavidgraham/masscan) que permiten escanear a todo el espacio IPv4 en pocos minutos, esos scans no son rigurosos ni detallados.

En cambio con shodan, es posible consumir datos de forma pasiva e instantánea. La versión gratis de sólo permite ver una lista limitada de resultados y no permite hacer descargas. Por lo tanto activé la suscripción de por vida por $50. Me parece una inversión super buena para alguien quien trabaja con IoT como yo.

## Análisis inicial

Me gusta comenzar con una visión en general sobre los datos. Así recibo una noción sobre las preguntas que podría responder el dataset. Luego de ver ejemplos en la documentación, me hice una idea de lo que es posible guiándome con la [referencia de los filtros](https://beta.shodan.io/search/filters).

Usando la consola de Shodan, fijémonos en las vulnerabilidades actualmente más frecuentes del Paraguay. Lo preocupante de estas estadísticas es que algunas vulnerabilidades ya son del 2014, es decir hay miles de dispositivos que hace años no recibieron una actualización de software.

![Bild](https://pbs.twimg.com/media/Ejb2bh-XcAAMt8R?format=png&name=large)

La primera columna contiene el identificador, y la segunda el conteo de las veces que aparece

En la este query vemos los top 10 sistemas operativos, ISPs (proveedores de internet) y ciudades con el conteo de vulnerabilidades en forma descendiente.

![Bild](https://pbs.twimg.com/media/Ejb4tK2XYAEaW_o?format=png&name=large)

El software en donde más vulnerabilidades ocurren es lighttpd. Lighttpd es un un servidor web muy liviano y eficiente por lo cual sospecho que está deployado en muchos routers y equipos locales del cliente ([CPEs](https://es.wikipedia.org/wiki/Customer_Premises_Equipment)).

![](/assets/images/imagen-1024x493.png)

Aquí vemos los puertos más vulnerables. Los puertos 8080, 8000 y 8888 son bien conocidos como puertos que se utilizan en el desarrollo de software. Los entornos de desarrollo no se deben exponer al Internet, ya que no cuentan con la misma configuración de seguridad que un entorno de producción. *Si sos programador y tienes un entorno de desarrollo, asegúrate de que solo sea accesible desde la red interna*.

![](/assets/images/imagen-1-1024x459.png)

Para saciar mi curiosidad, comparé a la distribución de versiones TLS/SSL de Paraguay con China y EEUU. Curiosamente es similar en los tres países, aunque [China bloqueó TLS 1.3 con ESNI](https://www.zdnet.com/article/china-is-now-blocking-all-encrypted-https-traffic-using-tls-1-3-and-esni/). ESNI esconde los sitios a los que se está accediendo, evadiendo así vigilancia y censura.

![Bild](https://pbs.twimg.com/media/EjcH-stXcAAHm98?format=png&name=large)

## Cómo protegerse en el IoT

Básicamente hay dos formas de protegerse. La primera es actualizar al software puntualmente para que cualquier vulnerabilidad nueva no tarde en ser parchada. La segunda opción es no exponerse al internet.

Por supuesto que lo mejor es la combinación de ambas prácticas. Minimizar la superficie de ataque al sólo exponer lo que debe estar expuesto como servidores web, y mantener a todo software actualizado por más que no esté directamente expuesto al Internet.

A continuación muestro un ejemplo de cómo suelo configurar los firewalls usando RouterOS.

---

### Ejemplo de configuración de Firewall en RouterOS

```
/ip firewall address-list
add address=190.112.168.2 list=Admins
add address=192.168.1.3 list=Admins

/ip firewall filter
add action=accept chain=input comment="Allow connections from router to internet" connection-state=established,related
add action=accept chain=input comment="Allow Admins" src-address-list=Admins
add action=drop chain=input comment="Drop Everything Else"
```

En líneas 1-3 agrego las IPs públicas de los Admins que sí deben poder acceder al router. Luego en ip firewall filter agregamos 3 reglas. Es importante respetar al orden ya que el firewall ejecuta a la cadena del firewall desde arriba hacia abajo. La primera regla deja pasar conexiones establecidas y relacionadas. Esto es útil si uno quiere hacer actualizaciones del firmware del router.

La segunda regla le da acceso a las IPs registradas en la address-list de los Admins. Esto es útil si se necesita acceder al router desde Internet para dar soporte o para establecer VPNs.

En la tercera regla se hace drop de todo el resto del trafico que está destinado al router. Es decir se bloquea absolutamente todo, menos lo que proviene de las IPs autorizadas o del router mismo a la hora de actualizarse.
