---
layout: post
title:  "C vs Go vs pypy vs Python vs Javascript V8"
date:   2015-09-28
categories: jekyll update
category: ES
comments: true
---

Siempre me gusta experimentar con performance de algoritmos y lenguajes de programación. Esta vez hice una simple comparación de velocidad entre Go, C, pypy y python. El algoritmo consiste en un loop simple que suma los números de 1 a 10.000.000

Para mi gran sorpresa el ganador es Go y no C, como esperado. Todavía no se a que se debe eso pero hare un update al post cuando tenga la respuesta, estoy seguro que me olvide de alguna optimización en el código C. 

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
    printf("sum: %ld\n", sum);
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

**Update 1**  
Agregué un test con NodeJs (como pude olvidarme de eso?)
{% highlight javascript %}
var sum = 0;
for (var i = 0; i < 10000000; i++) {
  sum+=i;
}
console.log(sum);
{% endhighlight %}

Javascript realmente parece ser el lenguaje interpretado mas rápido, es increíble que tarde solo 2.4 veces mas que C
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/nodejs.png)

###**Update 2 misterio resolvido?**
Como mostraron en [Reddit](https://www.reddit.com/r/compsci/comments/3mss9b/any_idea_why_this_go_loop_is_faster_than_pure_c/) y los comentarios en el post en [ingles](http://karlheinzniebuhr.github.io/en/2015/09/28/C-vs-Go-vs-pypy-vs-Python/), usando [CFLAGS](https://wiki.gentoo.org/wiki/GCC_optimization) para activar la optimización del codigo C aumenta drásticamente la velocidad. También tuve que inicializar la variable sum porque de lo contrario retornaba un resultado erróneo.  
{% highlight c %}
#include <stdio.h>
 
int main ()
{
   long a;
   long sum = 0;
   /* for loop execution */
   for( a = 0; a < 10000000; a++ )
   {
      sum += a;
   }
    printf("sum: %ld\n", sum);
   return 0;
}
{% endhighlight %}



El código C optimizado corre 5x mas rápido comparado con el binario hecho sin utilizar CFLAGS y es 40% mas rápido que Go. Nótese que usando la optimización  en C, el compilador pre calcula el resultado del loop, asi que en caso que el binario de Go corre el loop cada vez, esta comparación no es justa. 
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-opt.png)

###**Update 3: Go sigue siendo si no se puede aplicar optimización en C**

Para prevenir que C precompile el resultado del loop, hice los tests nuevamente pasando el numero como parámetro en la linea de comando. 

código C con parametro 
{% highlight c %}
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>

main(int argc, char *argv[])
{

  int arg1 = 1;

    arg1 = atoi(argv[1]);

   long a;
   long sum = 0;
   /* for loop execution */
   for( a = 0; a < arg1; a++ )
   {
      sum += a;
   }
    printf("sum: %ld\n", sum);
   return 0;
}
{% endhighlight %}

código Go con parametro
{% highlight c %}
package main

import "os"
import "fmt"
import "strconv"

func main() {
  arg := os.Args[1]

  n, e := strconv.Atoi(arg)
  if e != nil {
      fmt.Println(e)
  }

  sum := 0
  for i := 0; i < n; i++ {
    sum += i
  }
  fmt.Println(sum)
}
{% endhighlight %}

C tiene la misma velocidad que antes sin optimización.  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-cmd.png)

Pero Go sigue manteniendo su velocidad, es 3 veces mas rápido que C extrañamente.  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go-cmd.png)


