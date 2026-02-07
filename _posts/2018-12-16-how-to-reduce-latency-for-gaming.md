---
layout: post
title: "How to reduce latency for gaming"
date: 2018-12-16 09:25:29 +0000
categories: [Blog]
tags: [Technology]
---

When having problems with latency the first advice is to check the distance of the server and issues with your Internet Service Provider. But there is something that might cause you problems if you have a slow Internet connection, bandwidth (BW) usage.

To illustrate how BW usage can cause a rise in latency lets take a look at the following graph.

![](/assets/images/2Mbps1.png)

First I made a download with a 2Mbps connection limited by a Mikrotik queue speed limiter, as we can see the ping from the local network was about 35ms on average. Then I set the queue limiter to 10 Mbps and immediately the ping went down to about 10ms. Finally with 30 Mbps, the ping went down to about 1-2ms which is normal on a local optical network.

The lesson here is, if you have a slow connection, try to disable all Internet using devices if you want to get the best latency for your game. Or just get more BW. 😁

The reason the above happens is because the Router which limits your BW has to check all the packets going to your home router, once a threshold is surpassed, packets are dropped and slowed down.
