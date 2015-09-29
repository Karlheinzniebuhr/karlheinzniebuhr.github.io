---
layout: post
title:  "C vs Go vs pypy vs Python"
date:   2015-09-28
categories: jekyll update
category: EN
comments: true
---

I love to perform benchmarking tests and try to optimise algorithms or compare implementations in different languages. This time I compared Go, C, pypy and Python with a simple loop which sums all numbers between 1 and 10.000.000

To my big surprise, the winner wasn’t C but Go. I have no idea why but as soon as I know I’ll update this post, maybe somebody can answer that question in the comments. For sure there is a way to further optimise the C code. 

Hardware specs  
MacBook Pro (Retina, 13-inch, Early 2015)  
Processor 2.7 GHz Intel Core i5  
Memory 8 GB 1867 MHz DDR3  

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
    printf("sum: %lu\n", sum);
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

Updates coming soon


