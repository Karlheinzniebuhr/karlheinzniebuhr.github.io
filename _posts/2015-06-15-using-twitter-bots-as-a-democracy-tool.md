---

layout: post
title:  "Using Twitter-bots as a democracy tool"
date:   2015-06-15
categories: [Blogging]
tags: [Blogging, Culture]
banner_image: pyrawebs.jpg
archived: true
---

<h5>By Karlheinz Niebuhr, follow me on <a href="https://twitter.com/NiebuhrKarl">twitter</a>, and <a href="https://github.com/Karlheinzniebuhr">github</a></h5>

***Background information***: On Thursday morning 04.06.15 the Paraguayan Senate defeated a mandatory data retention bill that would have compelled local ISPs to retain communications and location details of every user for a period of 12 months.<A HREF="#1">[1]</A>
<!--more-->
###Introduction
A key tool which was used by Paraguayans to fight the data retention law is a python script named “Pyrawebs”. The name of the Tool which sends automated tweets to the Paraguayan politicians, alludes to the digital version of pyragües, informers who monitored the civilian population’s movements on behalf of dictator Alfredo Stroessner, who ruled between 1954 and 1989. In this post I will explain how this script works and how it was used. Hopefully someone else can give it a meaningful use.

###How it works  
The tools which is written in python by <a href="https://twitter.com/juanbaezr">Juan</a> and <a href="https://twitter.com/melizeche">Marce</a> uses the [tweepy library](https://github.com/tweepy/tweepy) to communicate with the twitter API. It can be executed via the command line and takes as input the names of two text files. One of them a list of Twitter users and the other one is the file which contains a list of all the tweets you want to send.
IMAGES
It iterates over every tweet and sends them to every single user contained in the users text file.

###Evading spam patrol
One of the issues we encountered was an error message after a number of consecutive tweets.    
***"This request looks like it might be automated. To protect our users from spam and other malicious activity, we can't complete this action right now. Please try again later."***  
Apparently the twitter API wasn’t amused.  
Fortunately I could solve this by rising the inferior time limit of the random time function. The twitter API gets suspicious if there are several new tweets in a short time period (Twitter engineers if you are reading this, don't update your code.) And that’s it, now you can deliver meaningful tweets 24/7.  
Cheers


#### [I'll post the main code below, for more details check it out on Github](https://github.com/Karlheinzniebuhr/pyrawebs)

#### pyrawebs.py
{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import random
from random import randint
from time import sleep

#from our keys module (keys.py), import the keys dictionary
from my_own_keys import keys

CONSUMER_KEY = keys['CONSUMER_KEY']
CONSUMER_SECRET = keys['CONSUMER_SECRET']
ACCESS_TOKEN = keys['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = keys['ACCESS_TOKEN_SECRET']

def oauth_login(consumer_key, consumer_secret,access_key,access_secret):
  """Authenticate with twitter using OAuth"""
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  return tweepy.API(auth)

if __name__ == "__main__":
  api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  print "Authenticated as: %s" % api.me().screen_name

  l_tweets   = []
  l_targets  = []

  arg_tweets  = str(sys.argv[1])
  arg_target  = str(sys.argv[2])

  f_tweets   = open(arg_tweets,'r')
  f_targets  = open(arg_target,'r')

  s_tweets   = f_tweets.readlines()
  s_targets  = f_targets.readlines()

  # create list of target twitter accounts
  for line in s_targets:
    l_targets.append(line.strip().decode('utf-8'))

  # create list of tweets
  for line in s_tweets:
    l_tweets.append(line.strip().decode('utf-8'))

  # create and send the tweets
  for tweet in l_tweets:
    actual_target = '@'
    for target in l_targets:
      tweet   = tweet.replace(actual_target, target)
      if target != '':
        actual_target = target
      print tweet

      try:
        api.update_status(status=tweet)
        wait = randint(30,120)
        print 'wait: '+str(wait)+' seconds'
        time.sleep(wait)
      except Exception as exception:
        print exception
        print "Failed to tweet:", tweet

{% endhighlight %}

#### key file key.py
{% highlight python %}
#!/usr/bin/env python
#keys.py
#visit http://dev.twitter.com to create an application and get your keys
keys = dict(
CONSUMER_KEY = 'vlXuFjAa$3FGsdWMpemVQ',
CONSUMER_SECRET = 'L1IKV1DUKKWs4gsdG3x2OUHt6Bby6uJLyhtgX7OUrNigwwb',
ACCESS_TOKEN = 'e74DNGbuIwUd1xNOPDCXpMr3XYSCXpMr3XYPCCCSwIzZ',
ACCESS_TOKEN_SECRET = '8d8O2ZjuoTIUGXjbHCoJqpYxd13KtqxYhrX'
)
# Don't even think of it, those are fake
{% endhighlight %}

#### list of target twitter accounts.. insert as many as you like  
{% highlight bash %}
@target1
@target2
@target3
@target4
@target5
@target6
@target7
{% endhighlight %}

#### list of tweets.. you can insert as many as you like
{% highlight bash %}
@ Inconstitucional, desproporcionado, innecesario: ¡Diga no a #pyrawebs! eff.org/r.q0e5
@ basta ya del espionaje, no a los #pyrawebs
@ usted va a pagar de su propio bolsillo el aumento del costo del internet? #pyrawebs
{% endhighlight %}


# [Check out the code and tutorial on Github](https://github.com/Karlheinzniebuhr/pyrawebs)



Resources:  <br>
<A NAME="1" href="https://www.eff.org/deeplinks/2015/06/turning-tide-against-online-spying-paraguay">[1] https://www.eff.org/deeplinks/2015/06/turning-tide-against-online-spying-paraguay</A>  <br>
