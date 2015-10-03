---
layout: post
title:  "C vs Go vs pypy vs Python vs Javascript V8"
date:   2015-09-28
categories: jekyll update
category: EN
comments: true
---

I love to perform benchmarking tests and try to optimise algorithms or compare implementations in different languages. This time I compared Go, C, pypy and Python with a simple loop which sums all numbers between 1 and 10.000.000

To my big surprise, the winner wasn’t C but Go. I have no idea why but as soon as I know I’ll update this post, maybe somebody can answer that question in the comments. For sure there is a way to further optimise the C code. 

**Specs**  
MacBook Pro (Retina, 13-inch, Early 2015)  
Processor 2.7 GHz Intel Core i5  
Memory 8 GB 1867 MHz DDR3  

C compiler: clang-700.0.75  
Go version go1.5.1 darwin/amd64  
PyPy 2.6.0 with GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.40)  
Python 2.7.10  
Node v0.12.6  

This is the C code
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

Go
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

Python/pypy
{% highlight python %}
sum = 0
for i in range(10000000):
    sum+=i
print(sum)
{% endhighlight %}


As you can see, C is pretty damn fast, it takes only 0.03 seconds to sum up everything. 

![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c.png)

Python takes 1.75 seconds 
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/python.png)

Pypy took 0.26 seconds the first time
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/pypy1.png)

The second time it took only 0.101 which is only 3 times slower than the C implementation
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/pypy2.png)

But the indisputable winner was Go which took only 0.010 seconds, 3x faster than C.
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go.png)


**Update 1**  
I added a test with NodeJs
{% highlight javascript %}
var sum = 0;
for (var i = 0; i < 10000000; i++) {
  sum+=i;
}
console.log(sum);
{% endhighlight %}

Amazing, JS really seems to be the fastest interpreted language.. just 0.077 seconds! 2.4 times slower than unoptimised C and about 31% faster than pypy
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/nodejs.png)

###**Update 2 Problem solved**
As pointed out on [Reddit](https://www.reddit.com/r/compsci/comments/3mss9b/any_idea_why_this_go_loop_is_faster_than_pure_c/) and the comments, using [CFLAGS](https://wiki.gentoo.org/wiki/GCC_optimization) to activate code optimisation of the compiler increases the speed of C considerably. I also had to initialise the sum variable because otherwise it returned the wrong result. 
This is how I compiled 
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



Now the code runs 5x faster than C without using CFLAGS and 40% faster than Go.
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-opt.png)

####**Update 3: Changed the code with command line args for further testing**

To make sure that the output isn’t just a precomputed constant value made in compile time, I’ve adapted the code for command line arguments. Now I can pass any number I want, the tests where consistent with the previous measurements.  

C with command line argument  
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

The C assembly code I got with the following command is just 22 lines long  
{% highlight bash %}
$ otool -tvV loop_sum
{% endhighlight %}

{% highlight bash %}
(__TEXT,__text) section
_main:
0000000100000f20  pushq %rbp
0000000100000f21  movq  %rsp, %rbp
0000000100000f24  movq  0x8(%rsi), %rdi
0000000100000f28  callq 0x100000f5e             ## symbol stub for: _atoi
0000000100000f2d  xorl  %esi, %esi
0000000100000f2f  testl %eax, %eax
0000000100000f31  jle 0x100000f4b
0000000100000f33  movslq  %eax, %rcx
0000000100000f36  leaq  -0x1(%rcx), %rax
0000000100000f3a  leaq  -0x2(%rcx), %rdx
0000000100000f3e  mulq  %rdx
0000000100000f41  shldq $0x3f, %rax, %rdx
0000000100000f46  leaq  -0x1(%rcx,%rdx), %rsi
0000000100000f4b  leaq  0x3e(%rip), %rdi        ## literal pool for: "sum: %ld\n"
0000000100000f52  xorl  %eax, %eax
0000000100000f54  callq 0x100000f64             ## symbol stub for: _printf
0000000100000f59  xorl  %eax, %eax
0000000100000f5b  popq  %rbp
0000000100000f5c  retq

{% endhighlight %}



Go with command line argument
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

The Go assembly code is 161.021 lines long which must be due to the static linking of Go.  
{% highlight bash %}
$ otool -tvV loop_sum_go  
{% endhighlight %}  
<a href="https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/data/assembly/go_assembly.txt.zip" download>Download Go assembly code</a>

C  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-cmd.png)


What also is interesting is that it doesn’t seem to matter much if I pass in bigger numbers, here trying with 1.000.000.000  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/c-cmd2.png)

Go  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go-cmd.png)

Go takes considerably longer with 1.000.000.000  
![Image image1](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/ES/_posts/img/go-cmd2.png)
