---
layout: post_es
title:  "Experimento en curso de udacity que llevó a una libreria python."
date:   2015-05-10
categories: jekyll update
category: ES
comments: true
---

#### La historia por detrás de la libreria [Pythonbenchmark](https://github.com/Karlheinzniebuhr/pythonbenchmark/)

#####<A HREF="#libreria">Saltar la historia</A>

#### La historia
Todo empezó en el curso de <a href="https://www.udacity.com/course/cs101" target="_blank">CS 101</a>&nbsp;en <span class="lG">Udacity</span> donde gracias a&nbsp;<a href="https://twitter.com/antoniogbo" target="_blank">Un amigo</a>&nbsp;que conocí en el foro me metí en un análisis interesante.

Se trataba de dos algoritmos para hacer una [tabla hash](http://es.wikipedia.org/wiki/Tabla_hash) para un [motor de búsqueda](http://es.wikipedia.org/wiki/Motor_de_b%C3%BAsqueda). El poder de los motores de búsqueda consiste en la velocidad con la cual logran asociar terminos de búsqueda con cientos de millones de posibles resultados. La arquitectura que utilizan motores de búsqueda como google es mucho mas compleja hablando de la totalidad pero se basan en algo bastante simple. Las tablas hash. Una tabla hash es una estructura de datos que asocia llaves o claves con valores. Hasta ahí todo normal, nada tan especial, el problema es que si existen millones de registros, el buscador tendría que correr a través de todo el registro cada vez que alguien haga una búsqueda, simplemente sería demasiado costoso y lento.  Publicaré otro post explicando como se soluciona este problema, ahora siguiendo con el tema del curso. Según el <span class="lG">profesor</span>&nbsp;<a href="http://www.cs.virginia.edu/~evans/" target="_blank">David Evans</a>&nbsp;uno de los dos algoritmos que habíamos hecho en clases era más rápido, lo cual resultó no ser cierto como descubrió un amigo que abrió un&nbsp;<a href="http://forums.udacity.com/questions/100164089/challenging-the-professor-testing-times-need-your-help-to-analyze-this-fun-discovery" target="_blank">POST</a>&nbsp;en <span class="lG">el foro de Udacity</span>. Sólo le faltaba ayuda con el algoritmo de comparación. Esto capto inmediatamente mi interés y empece a dedicar mi sábado de noche a crear un algoritmo que tomaría nuestros dos algoritmos de la clase para comprobar cual de ellos es mas rápido. 

Después de muchas pruebas llegamos a la conclusión que el profesor estaba equivocado, le avise por Twitter y me respondió en poco tiempo lo cual me sorprendió, profesores tan abiertos a críticas quisiera haber tenido más en la facultad.  

[El link del tweet](https://twitter.com/UdacityDave/status/448893996517953536)

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/NiebuhrKarl">@NiebuhrKarl</a> <a href="https://twitter.com/antoniogbo">@antoniogbo</a> You are correct! Thanks for the notice - I&#39;ll post a longer discussion on this in the forum...</p>&mdash; David Evans (@UdacityDave) <a href="https://twitter.com/UdacityDave/status/448893996517953536">March 26, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Siguió con un mail y un post explicando el motivo por el cual la teoría en este caso no acertó, por una cuestión de cómo esta implementado algo en python mismo. Recomiendo leer el foro para entenderlo mas a detalle.
[El post completo](http://forums.udacity.com/questions/100164089/challenging-the-professor-testing-times-need-your-help-to-analyze-this-fun-discovery)

Este fue el mail de Dave:


<div style="margin:0px"><center><table style="border:20px solid rgb(229,235,248);margin:10px auto;width:750px;text-align:left"><tbody><tr><td style="padding:20px"><div><a href="http://forums.udacity.com/" style="border:0px" target="_blank"><img src="https://ci4.googleusercontent.com/proxy/wsN2DKbjBI7senlAjJqzk9lXNqjACOaM9trJgH04tbyoRY6Q7qCTBBQ6bOocCjdMu4M7ZXG2YoerCVWuqR-dlg=s0-d-e1-ft#http://forums.udacity.com/upfiles/logo.png" alt="Udacity Discussion Forum" border="0"></a><hr style="color:rgb(204,204,204);border:0px;min-height:1px;background-color:rgb(204,204,204);margin-bottom:20px">

<p style="color:rgb(51,51,51);font-family:'helvetica neue',arial,Helvetica,sans-serif;line-height:18px;font-size:14px;margin-top:10px">Hello Karlheinz Niebuhr,</p></div><p style="color:rgb(51,51,51);font-family:'helvetica neue',arial,Helvetica,sans-serif;line-height:18px;font-size:14px;margin-top:10px">

<a href="http://forums.udacity.com/users/100007336/udacitydave" style="color:rgb(48,96,168);text-decoration:none;font-weight:bold" target="_blank">UdacityDave</a>&nbsp;has just posted a new answer on <span class="lG">Udacity</span> Forums to the question&nbsp;<a href="http://forums.udacity.com/questions/100164089/challenging-the-professor-testing-times-need-your-help-to-analyze-this-fun-discovery" style="color:rgb(48,96,168);text-decoration:none;font-weight:bold" target="_blank">Challenging the <span class="lG">professor</span> :) Testing times - need your help to analyze this fun discovery!</a>:</p>

<blockquote><p>Thanks for pointing out the mistake and all the great discussion on this!</p><p>It does indeed look like my claim that it would be faster for very long strings to do the modulo inside the loop is incorrect.</p>

<p>The actual issues here are fairly complex, and depend a lot on how Python implements numbers and how the number of buckets is chosen. In many languages (including C and Java), normal numbers are represented using a fixed-size block of bits (e.g., a 32-bit integer). This means there is some maximum number that can be represented using an int (2**32 - 1 if it is an unsigned 32-bit integer), and if you do addition beyond that maximum value the number will wrap-around (without producing any visible error). So, in C adding one to a big number sometimes gives you 0 (or a big negative number, if the number is a signed type). Because of this, people who program in these languages have to think carefully about the order of operations to avoid strange results because of overflows, and it would definitely be necessary to do the modulo operator inside the loop.</p>

<p>In Python, numbers are implemented in a more complex way where a variable amount of storage can be used for each number and the largest numbers that can be represented are huge (there is no fixed maximum, but eventually, of course, the amount of memory available in your machine for the Python program will run out). So, we will get the correct answer regardless of whether the % is done inside or outside the loop.</p>

<p>The question of cost, then, depends on the costs of doing all the extra % operations versus the cost of doing all the arithmetic on large numbers. The cost of the modulo operator depends a lot on the actual value of the modulus. If it is a power of two and numbers are represented in some sensible binary format, we can do the modulo operation by just chopping off (or zeroing) all bits to the right of the modulus; even for big numbers, this should only take one machine instruction. If the modulus is an arbitrary number though, computing a % b requires doing a very expensive division. So, it makes sense that doing this everytime through the loop is more expensive than doing the big number additions and only one % operation.</p>

<p>My guess would be that if you pick the number of buckets as a power of two (e.g., 1024 instead of 1000), and try this experiment again on very long strings, that the version with the % inside the loop will actually be faster. But, I haven't done the experiments yet, so perhaps you will prove me wrong again!</p>

</blockquote><div><p style="color:rgb(51,51,51);font-family:'helvetica neue',arial,Helvetica,sans-serif;line-height:18px;font-size:14px;margin-top:10px">Don't forget to come over and cast your vote.</p><p style="color:rgb(51,51,51);font-family:'helvetica neue',arial,Helvetica,sans-serif;line-height:18px;font-size:14px;margin-top:10px">

Thanks,<br><span class="lG">Udacity</span> Forums</p><p style="color:rgb(51,51,51);font-family:'helvetica neue',arial,Helvetica,sans-serif;line-height:18px;font-size:14px;margin-top:10px">P.S. You can always fine-tune which notifications you receive&nbsp;<a href="http://forums.udacity.com/users/100113429/karlheinz-niebuhr/subscriptions/" style="color:rgb(48,96,168);text-decoration:none;font-weight:bold" target="_blank">here</a>.</p>

<hr style="color:rgb(204,204,204);border:0px;min-height:1px;background-color:rgb(204,204,204);margin-bottom:20px"><p style="color:rgb(51,51,51);font-family:'helvetica neue',arial,Helvetica,sans-serif;line-height:18px;font-size:14px;margin-top:10px">

<small style="font-family:'Lucida Grande',Trebuchet,Helvetica,sans-serif;font-size:12px"></small></p></div></td></tr></tbody></table></center></div><br>

## <A NAME="libreria">La librería</A>
Todo lo mencionado anteriormente pasó en 2014, un año mas tarde tuviendo una discusión en el chat con amigos programadores me puso a reutilizar ese código hecho para el curso para comparar dos algoritmos. El tema es el siguiente, [timeit](https://docs.python.org/2/library/timeit.html), el método que viene con la librería estándar de python permite medir el tiempo de ejecución de código esta diseñado para medir "code snippets".  [(Snippet es un término del idioma inglés utilizado en programación para referirse a pequeñas partes recusables de código fuente.)](http://es.wikipedia.org/wiki/Snippet) Lo cual no me gusta para nada en la mayoría de casos, mayormente quiero comparar dos funciones y ver cuál es mas eficiente. No conociendo a ninguna librería que permite hacer eso me puse a crear mi propia librería [https://github.com/Karlheinzniebuhr/pythonbenchmark/](https://github.com/Karlheinzniebuhr/pythonbenchmark/) . 

En el documento readme están las indicaciones pero lo mencionaré aquí brevemente en español. 

Básicamente hay dos formas de utilizarla, con el decorador, y llamando a la función compare() pasándo 2 funciones como parámetros. 

**Caso 1: Llamar utilizando el decorador**

{% highlight python %}

from pythonbenchmark import compare, measure
import time

a,b,c,d,e = 10,10,10,10,10
algo = [a,b,c,d,e]

def miFuncion(algo):
    time.sleep(0.4)

def miFuncionOptimizada(algo):
    time.sleep(0.2)

# test de comparación
compare(miFuncion, miFuncionOptimizada, 10, algo)


{% endhighlight %}

**Caso 2: Utilizando la función compare**

{% highlight python %}

from pythonbenchmark import compare, measure
import time

a,b,c,d,e = 10,10,10,10,10
algo = [a,b,c,d,e]

# se declaran los decoradores encima de las dos funciones a comparar
@measure
def myFunction(algo):
    time.sleep(0.4)

@measure
def myOptimizedFunction(algo):
    time.sleep(0.2)

# se llama a las funciones para que se ejecuten
myFunction(algo)
myOptimizedFunction(algo)


{% endhighlight %}


Si bien este método no esta tan preciso como el método timeit que viene inlcuido con python, es lo suficientemente preciso para la mayoría de casos. La precisión en este caso esta definida por la granularidad del reloj de la plataforma (sistema operativo) en donde se esta ejecutando el programa. 
Espero que a más personas les sirva la librería, recibo sugerencias y contribuciones con gusto.
Saludos


## *** UPDATE ***
La libreria ahora esta disponible en el gestor de paquetes PyPi. Podes instalarla con este comando:
{% highlight bash %}
pip install pythonbenchmark
{% endhighlight %}

