---

layout: post
title:  "C vs Go vs pypy vs Python vs Javascript V8"
date:   2015-09-28
categories: [Technology]
tags: [Technology]
banner_image: benchmark.jpg
archived: true
---

I love to perform benchmarking tests and try to optimise algorithms, or compare implementations in different languages. This time I compared Go, C, pypy, Python and JS with a simple loop which sums all numbers between 1 and 10.000.000

To my big surprise, at first the winner wasn’t C but Go. I had no idea why at first but eventually I found out. 
<!--more-->
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
{% include image_full.html imageurl="/images/posts/c.png" title="" caption="" %}

Python takes 1.75 seconds 
{% include image_full.html imageurl="/images/posts/python.png" title="" caption="" %}

Pypy took 0.26 seconds the first time 
{% include image_full.html imageurl="/images/posts/pypy1.png" title="" caption="" %}

The second time it took only 0.101 which is only 3 times slower than the C implementation 
{% include image_full.html imageurl="/images/posts/pypy2.png" title="" caption="" %}

But the indisputable winner was Go which took only 0.010 seconds, 3x faster than C. 
{% include image_full.html imageurl="/images/posts/go.png" title="" caption="" %}

**Update 1** 
I added a test with NodeJs
{% highlight javascript %}
var sum = 0;
for (var i = 0; i < 10000000; i++) {
 sum+=i;
}
console.log(sum);
{% endhighlight %}

Amazing, JS really seems to be the fastest interpreted language (I know).. just 0.077 seconds! 2.4 times slower than unoptimised C and about 31% faster than pypy
{% include image_full.html imageurl="/images/posts/nodejs.png" title="" caption="" %}

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
{% include image_full.html imageurl="/images/posts/c-opt.png" title="" caption="" %}

####**Update 3: Changed the code with command line args for further testing**

To make sure that the output isn’t just a precomputed constant value made at compile time, I’ve adapted the code for command line arguments. Now I can pass any number I want, the tests were consistent with the previous measurements.

C with command line argument 
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

The C assembly code I got with the following command is just 40 lines long 
{% highlight bash %}
$ gcc loop_sum.c -S
{% endhighlight %}

{% highlight bash %}
 .section __TEXT,__text,regular,pure_instructions
 .macosx_version_min 10, 10
 .globl _main
 .align 4, 0x90
_main: ## @main
 .cfi_startproc
## BB#0:
 pushq %rbp
Ltmp0:
 .cfi_def_cfa_offset 16
Ltmp1:
 .cfi_offset %rbp, -16
 movq %rsp, %rbp
Ltmp2:
 .cfi_def_cfa_register %rbp
 movq 8(%rsi), %rdi
 callq _atoi
 xorl %esi, %esi
 testl %eax, %eax
 jle LBB0_2
## BB#1: ## %.lr.ph
 movslq %eax, %rcx
 leaq -1(%rcx), %rax
 leaq -2(%rcx), %rdx
 mulq %rdx
 shldq $63, %rax, %rdx
 leaq -1(%rcx,%rdx), %rsi
LBB0_2:
 leaq L_.str(%rip), %rdi
 xorl %eax, %eax
 callq _printf
 xorl %eax, %eax
 popq %rbp
 retq
 .cfi_endproc

 .section __TEXT,__cstring,cstring_literals
L_.str: ## @.str
 .asciz "sum: %ld\n"
.subsections_via_symbols
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
<a href="karlheinzniebuhr.github.io/data/assembly/go_assembly.txt.zip" download>Download Go assembly code</a>

C 
{% include image_full.html imageurl="/images/posts/c-cmd.png" title="" caption="" %}

What also is interesting is that it doesn’t seem to matter much if I pass in bigger numbers, here trying with 1.000.000.000 
{% include image_full.html imageurl="/images/posts/c-cmd2.png" title="" caption="" %}

Go 
{% include image_full.html imageurl="/images/posts/go-cmd.png" title="" caption="" %}

Go takes considerably longer with 1.000.000.000 
{% include image_full.html imageurl="/images/posts/c-cmd2.png" title="" caption="" %}

####To sum it up 
I noticed that the optimised code executes in constant time, no matter what number I throw at it. Suspecting that the compiler did a trick there, as mentioned I changed the code to pass the number as command line parameter. Doing so I made sure that the result itself wasn’t precomputed. Despite that the response time remained constant, so the only remaining logical explanation was that the compiler used math to compute the sum and it was confirmed in [this neat blogpost](http://blog.xebia.com/2015/10/05/gcc-compiler-optimizations-dissection-of-a-benchmark/). The nifty Clang compiler uses sum of an arithmetic sequence formula to get away with executing the task without doing the heavy lifting of the loop. Clever, but this shows that it is really hard to do fair benchmarks. 
Formula used by Clang to thrash the loop sum’s 
{% include image_full.html imageurl="/images/posts/sum_formula.png" title="" caption="" %}
After all, it seems that Go is faster at running the loop. I haven’t confirmed this in Go’s assembly code (perhaps someone can make a blogpost about that too :) ) but I think I can safely assume so because Go’s response time is proportional to the input number. 
I will certainly take a closer look at this so stay tuned.
