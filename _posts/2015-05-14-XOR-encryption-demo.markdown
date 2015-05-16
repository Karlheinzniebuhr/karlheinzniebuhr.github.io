---
layout: post
title:  "XOR encryption demo"
date:   2015-05-14
categories: jekyll update
category: EN
comments: true
---


#### A simple demo about XOR encryption ####
During the Stanford [Crypto-course](https://www.coursera.org/course/crypto) I made a demo in order to better understand the concept of XOR in encryption. 

[What is XOR?](http://en.wikipedia.org/wiki/Exclusive_or)

In digital cryptography basically everything comes down to XOR'ing things. This is such a simple concept but at the same time [it is the only existing mathematically unbreakable encryption.](http://users.telenet.be/d.rijmenants/en/onetimepad.htm) 

"In cryptography, a one-time pad (OTP) is an encryption technique that cannot be cracked if used correctly. In this technique, a plaintext is paired with a random secret key (or pad). Then, each bit or character of the plaintext is encrypted by combining it with the corresponding bit or character from the pad using modular addition. If the key is truly random, is at least as long as the plaintext, is never reused in whole or in part, and is kept completely secret, then the resulting ciphertext will be impossible to decrypt or break" ~ Wikipedia

[here is a video from Khanacademy explaining OTP.](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/one-time-pad)

[Click here for a more extensive explanation and the history behind OTP encryption. ](http://users.telenet.be/d.rijmenants/en/onetimepad.htm)

**So I decided to make a proof of concept, this is what I came up with.**  
Check out my code on [Github](https://github.com/Karlheinzniebuhr/XOR-encryption-demo/) or just [try it online.](https://repl.it/oJl)  
We take a keyboard input from the user (**message**), and generate a random password with the **same length**.
***Note that it's important that the password has the same length than the message.***

This is the entire script
{% highlight python %}
import random
import string

# XOR the message and key
# Exclusive disjunction or exclusive or is a logical operation that outputs true whenever both inputs differ (one is true, the other is false)
# http://en.wikipedia.org/wiki/Exclusive_or
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



def toBin(string):
	return ''.join('{:08b}'.format(ord(c)) for c in string)

def toAsc(bin_text):
	return ''.join(chr(int(bin_text[i:i+8], 2)) for i in xrange(0, len(bin_text), 8))

message = raw_input('--> ')
print("Message: " + message)
message_bit_string = toBin(message)

key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len(message)))
print("Key:", key)
key_bit_string = toBin(key)

encrypted_message = xor(message_bit_string, key_bit_string)
print("encrypted message in binary = " + encrypted_message + '\n')
print("encrypted message in ASCII = " + toAsc(encrypted_message) + '\n')

print("decrypt message with the password")
decrypted_message = xor(encrypted_message, key_bit_string)
print("message decrypted = " + str(decrypted_message == message_bit_string))
print("message in binary is: " + '"' + str(decrypted_message) + '"\n\n')
print("message in Ascii is: " + '"' + toAsc(str(decrypted_message)) + '"\n\n')
{% endhighlight %}


The function that does the encryption is the following. It takes two bit strings as input (the message and the key), iterates over them and applies XOR to every bit.

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


Output
![Image image2](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/images/xor.PNG)


Feel free to experiment with the code, I hope someone will find this as useful as I did to get a better understanding of the XOR encryption process. Questions are welcome. 
[https://github.com/Karlheinzniebuhr/XOR-encryption-demo/](https://github.com/Karlheinzniebuhr/XOR-encryption-demo/ "XOR-encryption-demo")

