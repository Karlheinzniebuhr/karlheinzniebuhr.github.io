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

**Especificaciones del sistema**  
MacBook Pro (Retina, 13-inch, Early 2015)  
Processor 2.7 GHz Intel Core i5  
Memory 8 GB 1867 MHz DDR3  

C compiler: clang-700.0.75  
Go version go1.5.1 darwin/amd64  
PyPy 2.6.0 with GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.40)  
Python 2.7.10  
Node v0.12.6  

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
NodeJs (como pude olvidarme de eso?)
{% highlight javascript %}
var sum = 0;
for (var i = 0; i < 10000000; i++) {
  sum+=i;
}
console.log(sum);
{% endhighlight %}

Javascript realmente parece ser el lenguaje interpretado mas rápido, es increíble que tarde solo 2.4 veces mas que C
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/nodejs.png)

**Update 1.1**  
Agregue un test en Java por pedido de los lectores. El resultado tomado es la segunda ejecución para dejar que tenga un ‘warm-up’ la JVM. 
También dividi en dos partes la prueba, la primera prueba usando el long primitivo de Java y en la segunda el tipo Java.lang.Long class.

Codigo usando long  
{% highlight java %}
public class Loop_sum {
  public static void main(String[] args) {
          long sum = 0;

          for (int i = 0; i < 10000000; i++) {
                sum += i;
          }
          System.out.println(sum);
  }
}
{% endhighlight %}

Codigo usando Java.lang.Long Class  
{% highlight java %}
public class Loop_sum {
  public static void main(String[] args) {
          Long sum = new Long(0);

          for (int i = 0; i < 10000000; i++) {
                sum += i;
          }
          System.out.println(sum);
  }
}
{% endhighlight %}

Resultado long
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/java-primitive.png)

Resultado Java.lang.Long Class
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/java-object.png)

Se puede ver que usando el tipo de dato primitivo es ligeramente mas rápido. Lo cual seguramente es debido al overhead generado por la encapsulación. 


###**Update 2 misterio resolvido**  
Como mostraron en [Reddit](https://www.reddit.com/r/compsci/comments/3mss9b/any_idea_why_this_go_loop_is_faster_than_pure_c/) y los comentarios en el post en [ingles](http://karlheinzniebuhr.github.io/en/2015/09/28/C-vs-Go-vs-pypy-vs-Python/), usando [CFLAGS](https://wiki.gentoo.org/wiki/GCC_optimization) para activar la optimización del codigo C aumenta drásticamente la velocidad. También tuve que inicializar la variable sum porque de lo contrario retornaba un resultado erróneo. Use CFLAGS de la siguiente manera:
{% highlight bash %}
$ gcc -O3 -march=native loop_sum.c -o loop_sum
{% endhighlight %}
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



El código C optimizado corre 5x mas rápido comparado con el binario hecho sin optimización y es 40% mas rápido que Go. 
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-opt.png)

####**Update 3: Adapte el código para pasar el numero de Loops como parámetro desde la linea de comandos**

Para asegurar que el resultado no fue precalculado en tiempo de compilación, adopte el código para que se pueda usar con parámetro desde la linea de comandos. Ahora se puede hacer la prueba con cualquier numero y el compilador no tiene forma de precalcular el resultado y devolver solo una constante. 

Código C con parametro  
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

Código Go con parametro
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

C  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-cmd.png)


Lo que también es interesante es que no parece impactar en el tiempo de ejecución el tamaño del numero que le paso, en esta prueba le pase 1.000.000.000
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-cmd2.png)

Go  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go-cmd.png)

Go toma un tiempo considerablemente mayor con el numero 1.000.000.000  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go-cmd2.png)
