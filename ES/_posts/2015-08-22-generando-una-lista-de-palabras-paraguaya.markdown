---
layout: post
title:  "Generando un diccionario de palabras Paraguayo"
date:   2015-08-22
categories: jekyll update
category: ES
comments: true
permalink: 2015-08-22/diccionario-de-palabras-Paraguayo
---


**Introducción**  
En este post explicare como hice algunos diccionarios de palabras para romper [hash's](https://es.wikipedia.org/wiki/Funci%C3%B3n_hash) de contraseñas. 
**Pero para que se usan las listas de palabras en el contexto de hacking?** 
Se utilizan para un método de cracking en donde se intenta averiguar una contraseña probando todas las palabras del diccionario. Este método suele ser mucho mas eficiente que los ataques de fuerza bruta en donde se intentan todas las posibles combinaciones de letras, números y/o signos. 
Para ver por qué es así basta con un simple ejemplo. Supongamos que queremos crackear la contraseña “**crackme**”. Probando con fuerza bruta,  suponiendo que la contraseña consiste solamente de letras en minúscula, necesitaríamos:
**27<sup>7</sup> = 10,460,353,203** posibles pruebas hasta adivinar la contraseña. 
27 letras del alfabeto elevado por la cantidad de letras o la longitud de la contraseña. 
Y si se usan letras en mayusculas, números y longitud 10 esta cifra se agranda bastante. 
**“crAckMe123” = ((27*2)+10)<sup>10</sup> = 1.152921505 x 10<sup>18</sup> posibilidades**. Un 115 con 16 ceros.
Números de esa magnitud con [slow hash's](http://crypto.stackexchange.com/questions/24/what-makes-a-hash-function-good-for-password-hashing) tardarían mucho tiempo en procesarse. Hasta con las tarjetas de video mas potentes.  Por eso en muchos casos es mas factible un ataque con un diccionario de palabras.  Por ejemplo para romper el Hash WPA2 del WIFI. 

Los diccionarios se producen de forma que ya casi siempre incluyen palabras como “crackme123”. Es un fenómeno conocido que las personas tienden a agregar números al final de sus contraseñas, probablemente lo hayas hecho también. Si en este momento su contraseña sigue siendo de esta forma “MiConTraseÑa123” te recomiendo cambiar por algo como “MiCon321TraseÑa”. ;)   

**Un diccionario para el Paraguay?** 
Los diccionarios de palabras se suelen crear para un lenguaje o un lugar/empresa en especifico. Mientras mas especifico el diccionario mas eficiente el ataque. Resulta que en nuestro país usamos palabras poco comunes en otras partes del mundo. Obviamente esta el guaraní pero hasta el castellano tiene ciertas palabras que uno no encuentra en las listas de palabras descargadas de internet. Por este motivo decidí hacer mi propio diccionario. 

**El proceso de armar el diccionario**
Me puse a pensar que la forma mas fácil de generar una lista de palabras seria coleccionar palabras de paginas web y foros paraguayos de forma automática con ayuda de un script. No tardé en encontrar una herramienta existente para realizar esta tarea llamada [CeWL](https://digi.ninja/projects/cewl.php). 
Empecé con el foro http://www.lajaula.com.py/ en el cual deje que la [araña web](https://es.wikipedia.org/wiki/Ara%C3%B1a_web) de CeWL entre a profundidad 3. La profundidad o “hops” en ingles son la cantidad de links que se aleja la araña web desde la pagina central. 
![enter image description here](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/images/hops.png)

En esta imagen ya se ve un patron de palabras muy familiares en nuestro país.
![enter image description here](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/images/captura-dict-lajaula.png)

Luego procese la pagina de abc-color, ultimahora, datamexguarani, portalguarani y el foro paraguayo en skyscrapercity ademas de unas otras paginas que prefiero no nombrar por seguridad. En cada pagina coleccionaba entre 20 y 55.000 palabras únicas. Ahora solo quedaba unificar todos los diccionarios y eliminar las palabras duplicadas. 
En esta tarea los comando bash son la mejor ayuda. Primero puse los diferentes diccionarios en una carpeta. 
Luego junte, odene y elimine los duplicados. 

{% highlight bash %}
cat abcColor datamexguarani lajaula personal portalguarani skycraperPy tigo ultimahora | sort | uniq > dictPy.txt
{% endhighlight %}

Me quede con una lista de **184406** palabras únicas. 
El diccionario se puede descargar en este enlace. 
<h3><a href="https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/data/wordlists/dictPy.txt" download>Descargar DictPy</a></h3>
Recomiendo usarlo en combinacion con reglas de [hashcat](http://hashcat.net/oclhashcat/) por ejemplo la **best64.rule**.

Un tiempo atrás también hice un diccionario con los números telefonicos móvil del Paraguay (mucha gente utiliza su número como contraseña del wifi por ejemplo). Para ello utilize el generador de listas de palabras [crunch](http://adaywithtape.blogspot.com.au/2011/05/creating-wordlists-with-crunch-v30.html).

Básicamente tome los prefijos mas utilizados y le agregue todas las combinaciones posibles de 6 dígitos (fuerza bruta) o sea **10<sup>6</sup>** = 1.000.000 números.
0961
0971 
0973 
0981 
0982
0984 
0985 
0991 
En total la lista contiene 8.000.000 números vs los **10<sup>10</sup>** = 10,000,000,000 que se utilizarían usando solamente fuerza bruta. 

<h3><a href="https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/data/wordlists/NumerosTelPY.txt" download>Descargar Dict-Numeros-Paraguay</a></h3>


Favor solo usar para hacking ético.  No me hago responsable del mal uso de los diccionarios. 