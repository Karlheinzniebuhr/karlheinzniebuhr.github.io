---
layout: post
title:  "C vs Go vs pypy vs Python"
date:   2015-09-28
categories: jekyll update
category: ES
comments: true
---

Siempre me gusta experimentar con performance de algoritmos y lenguajes de programación. Esta vez hice una simple comparación de velocidad entre Go, C, pypy y python. El algoritmo consiste en un loop simple que suma los números de 1 a 10.000.000

Para mi gran sorpresa el ganador es Go y no C, como esperado. Todavía no se a que se debe eso pero hare un update al post cuando tenga la respuesta, estoy seguro que me olvide de alguna optimización en el código C. 

Especificaciones del hardware  
MacBook Pro (Retina, 13-inch, Early 2015)  
Processor 2.7 GHz Intel Core i5  
Memory 8 GB 1867 MHz DDR3  

Este es el código C
{% highlight c %}
#include <stdio.h>
 
int main ()
{
   long a;
   long sum;
   /* for loop execution */
   for( a = 0; a < 10000000; a++ )
   {
        sum += a;
   }
    printf("sum: %lu\n", sum);
   return 0;
}
{% endhighlight %}

El código Go
{% highlight go %}
package main

import "fmt"

func main() {
    sum := 0
    for i := 0; i < 10000000; i++ {
        sum += i
    }
    fmt.Println(sum)
}
{% endhighlight %}

Y el abismalmente largo código Python/pypy
{% highlight python %}
sum = 0
for i in range(10000000):
    sum+=i
print(sum)
{% endhighlight %}


Como se puede ver, C es bastante rápido, solo tarda 0.03 segundos en sumar todo
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c.png)

Python tarda 1.75 segundos 
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/python.png)

Pypy la primera vez tardo 0.26 segundos
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/pypy1.png)

Y la segunda vez 0.101 lo cual apenas es 3 veces mas lento que la implementación en C
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/pypy2.png)

Pero Go arrasó con todo tardando solo 0.010 segundos
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go.png)

Actualizaré pronto con mas detalles.. 


