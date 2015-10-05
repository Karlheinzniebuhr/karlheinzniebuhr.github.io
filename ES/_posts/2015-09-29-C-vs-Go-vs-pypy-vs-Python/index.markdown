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

Codigo usando Java.lang.Long Class y Java.lang.Integer Class  
{% highlight java %}
public class Loop_sum {
  public static void main(String[] args) {
          Long sum = new Long(0);

          for (Integer i = new Integer(0); i < 10000000; i++) {
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

El código assembly de C que conseguí al compilar con el parametro -S tiene solo 40 lineas.  
{% highlight bash %}
$ gcc loop_sum.c -S 
{% endhighlight %}

{% highlight bash %}
  .section  __TEXT,__text,regular,pure_instructions
  .macosx_version_min 10, 10
  .globl  _main
  .align  4, 0x90
_main:                                  ## @main
  .cfi_startproc
## BB#0:
  pushq %rbp
Ltmp0:
  .cfi_def_cfa_offset 16
Ltmp1:
  .cfi_offset %rbp, -16
  movq  %rsp, %rbp
Ltmp2:
  .cfi_def_cfa_register %rbp
  movq  8(%rsi), %rdi
  callq _atoi
  xorl  %esi, %esi
  testl %eax, %eax
  jle LBB0_2
## BB#1:                                ## %.lr.ph
  movslq  %eax, %rcx
  leaq  -1(%rcx), %rax
  leaq  -2(%rcx), %rdx
  mulq  %rdx
  shldq $63, %rax, %rdx
  leaq  -1(%rcx,%rdx), %rsi
LBB0_2:
  leaq  L_.str(%rip), %rdi
  xorl  %eax, %eax
  callq _printf
  xorl  %eax, %eax
  popq  %rbp
  retq
  .cfi_endproc

  .section  __TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
  .asciz  "sum: %ld\n"
.subsections_via_symbols
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

El assembly de Go tiene 161.021 lineas de código, esto probablemente se debe en mayor parte a que Go usa static linking. En otras palabras, incluye todas las dependencias en el ejecutable ademas del garbage collector de Go.   
{% highlight bash %}
$ otool -tvV loop_sum_go  
{% endhighlight %}  
<a href="https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/data/assembly/go_assembly.txt.zip" download>Descargar assembly de Go</a>


C  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-cmd.png)

Lo que también es interesante es que no parece impactar en el tiempo de ejecución el tamaño del numero que le paso, en esta prueba le pase 1.000.000.000
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-cmd2.png)

Go  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go-cmd.png)

Go toma un tiempo considerablemente mayor con el numero 1.000.000.000  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go-cmd2.png)

####Resumiendo  
Como tal vez ya sospechaste, el compilador Clang de C esta usando una ecuación matemática para poder calcular la suma de cualquier numero N de loop’s en tiempo constante.  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/sum_formula.png)  
Alguien ya hizo un blogpost [aquí](http://blog.xebia.com/2015/10/05/gcc-compiler-optimizations-dissection-of-a-benchmark/) analizando el código assembly que genero.  
Después de todo, Go parece realizar mas rápidamente el loop, no lo comprobé en el código assembler de Go, pero creo que puedo asumirlo porque el tiempo de respuesta de Go es proporcional al numero que le paso como parámetro. Pero  al final C gana por evitarse el trabajo. Esto demuestra que es difícil realizar benchmarks justos. Pero hace que uno aprende mucho sobre los lenguajes en el proceso.  
Así que “stay tuned”  
Hasta pronto  
