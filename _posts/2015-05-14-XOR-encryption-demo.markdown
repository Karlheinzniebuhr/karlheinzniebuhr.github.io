---
layout: post
title:  "XOR encryption demo"
date:   2015-05-14
categories: jekyll update
category: EN
comments: true
---


#### A simple demo showing how to encrypt a message using XOR ####
During the Stanford [Crypto-course](https://www.coursera.org/course/crypto) I made a demo in order to better understand the concept of XOR in encryption. 

[http://en.wikipedia.org/wiki/Exclusive_or](http://en.wikipedia.org/wiki/Exclusive_or "What is XOR?")

Like the professor emphasized, in digital cryptography basically everything comes down to XOR'ing things. This is such a simple concept, and at the same time [the strongest encryption method in existence.](http://en.wikipedia.org/wiki/One-time_pad). 
Quoting Wikipedia: "In cryptography, a one-time pad (OTP) is an encryption technique that cannot be cracked if used correctly. In this technique, a plaintext is paired with a random secret key (or pad). Then, each bit or character of the plaintext is encrypted by combining it with the corresponding bit or character from the pad using modular addition. If the key is truly random, is at least as long as the plaintext, is never reused in whole or in part, and is kept completely secret, then the resulting ciphertext will be impossible to decrypt or break"

For a nice explanation of OTP encryption I recommend [this video from Khanacademy.](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/one-time-pad)

**This sounded a little magic to me so i decided to make a proof of concept, this is what I came up with.**  
In [this simple script](https://github.com/Karlheinzniebuhr/XOR-encryption-demo/) we take a keyboard input from the user (**message**), and generate a random password with the **same length**.
***Note that it's important that the password has the same length than the message.***

The function that does the XOR is the following. It takes two bit strings as input (the message and the key), iterates over them and applies XOR to every bit.

{% highlight python %}

def xor(a,b):
	bits = ''
	if not len(a) == len(b):
		return 'not equal length'

	for i in range(len(a)):
		if a[i] != b[i]:
			bits += '1'
		else:
			bits += '0'
	return bits

{% endhighlight %}


This code snippet generates the random key, we assume this to be a truly random string.

{% highlight python %}
key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len(message)))
{% endhighlight %}

These functions convert ASCII to Binary and vice versa.
{% highlight python %}
def toBin(string):
	return ''.join('{:08b}'.format(ord(c)) for c in string)

def toAsc(bin_text):
	return ''.join(chr(int(bin_text[i:i+8], 2)) for i in xrange(0, len(bin_text), 8))
{% endhighlight %}


finally, after executing we get as output
![Image image2](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/images/xor.PNG)


Feel free to experiment with the code, I hope someone will find this as useful as I did to get a better understanding of the XOR encryption process. Questions are welcome. 
[https://github.com/Karlheinzniebuhr/XOR-encryption-demo/](https://github.com/Karlheinzniebuhr/XOR-encryption-demo/ "XOR-encryption-demo")

