---
layout: post
title:  "OTP encryption demo"
date:   2015-05-14
categories: jekyll update
category: EN
comments: true
---

<h5>By Karlheinz Niebuhr, follow me on <a href="https://twitter.com/NiebuhrKarl">twitter</a>, and <a href="https://github.com/Karlheinzniebuhr">github</a></h5>

During the Stanford [Crypto-course](https://www.coursera.org/course/crypto) I made a demo about OTP encryption using the boolean "exclusive or" (XOR) function in order to better understand the concept behind it. 

[What is XOR?](http://en.wikipedia.org/wiki/Exclusive_or)

In digital cryptography basically everything comes down to XOR'ing things. It got my attention because his is such a simple concept but can be literally unbreakable when combined with OTP encryption. [OTP is the only mathematically proved unbreakable encryption.](http://users.telenet.be/d.rijmenants/en/onetimepad.htm) 

Now you may ask why I used OTP encryption in my demo. It turns out that OTP can be implemented with little code and therefore is perfect for a XOR example.

### One-time pad encryption
A one-time pad (OTP) is an encryption technique that cannot be cracked if used correctly. In this technique, a plaintext is paired with a random secret key (or pad). Then, each bit or character of the plaintext is encrypted by combining it with the corresponding bit or character from the pad using modular addition. If the key is truly random, is at least as long as the plaintext, is never reused in whole or in part, and is kept completely secret, then the resulting ciphertext will be impossible to decrypt or break.<A HREF="#1">[1]</A> 

To find key or plaintext, an adversary only has the random ciphertext at his disposal. This is an equation with two unknowns (the key and the message), which is mathematically unsolvable.  
If someone had infinite computational power he could go through all possible keys (a brute force attack). He would find out that applying the key XVHEU on ciphertext QJKES would produce the (correct) word TODAY. Unfortunately, he would also find out that the key FJRAB would produce the word LATER, and even worse, DFPAB would produce the word NEVER. He has no idea which key is the right one. In fact, you can produce any desired word or phrase from any one-time pad -encrypted message, as long as you use the 'right' wrong key. There is no way to verify if a solution is the right one. Therefore, the one-time pad system is proven completely secure.<A HREF="#2">[2]</A>

[For the keen readers: THis is a more extensive explanation about OTP and the history behind. ](http://users.telenet.be/d.rijmenants/en/onetimepad.htm)

**So all this was very exiting so I decided to make a proof of concept. This is what I came up with.**  
Check out my code on [Github](https://github.com/Karlheinzniebuhr/XOR-encryption-demo/) or just [try it online.](https://repl.it/oJl)  
The script takes a keyboard input from the user (**message**), and generates a random password with the **same length**.
***Note that it's important that the password has the same length than the message.***


This is the entire script
{% highlight python %}
import random
import string
import os

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
	return ''.join('{:08b}'.format(ord(character)) for character in string)

def toAsc(bin_text):
	return ''.join(chr(int(bin_text[i:i+8], 2)) for i in xrange(0, len(bin_text), 8))

message = raw_input('--> ')
print("Message: " + message)
message_bit_string = toBin(message)

key = os.urandom(len(message))
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


The function that does the encryption is the following. It takes two bit strings as input (the message and the key), iterates over them and applies XOR to every bit. This is symbolised by ⊕ and is represented by the following "truth table", where + represents "true" or 1 and − represents "false" or 0.

<table class="wikitable" style="margin: 1em auto 1em auto">
<tbody><tr bgcolor="#DDEEFF" align="center">
<td colspan="2"><b>INPUT</b></td>
<td><b>OUTPUT</b></td>
</tr>
<tr bgcolor="#DDEEFF" align="center">
<td><i><b>A</b></i></td>
<td><i><b>B</b></i></td>
<td><b><i>A</i> ⊕ <i>B</i></b></td>
</tr>
<tr bgcolor="#DDFFDD" align="center">
<td><b>−</b></td>
<td><b>−</b></td>
<td><b>−</b></td>
</tr>
<tr bgcolor="#DDFFDD" align="center">
<td><b>−</b></td>
<td><b>+</b></td>
<td><b>+</b></td>
</tr>
<tr bgcolor="#DDFFDD" align="center">
<td><b>+</b></td>
<td><b>−</b></td>
<td><b>+</b></td>
</tr>
<tr bgcolor="#DDFFDD" align="center">
<td><b>+</b></td>
<td><b>+</b></td>
<td><b>−</b></td>
</tr>
</tbody></table>


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


###**Update**
After some great [feedback on Reddit](https://www.reddit.com/r/crypto/comments/36jzji/short_and_easy_to_understand_otp_proof_of_concept/crepf6i) I made some updates to the code, namely switching to os.urandom() which is better suited for cryptographic use than random.choice(). 

Sources:  <br>
<A NAME="1">[1] http://users.telenet.be/d.rijmenants/en/onetimepad.htm</A>  <br>
<A NAME="2">[2] http://en.wikipedia.org/wiki/One-time_pad</A>