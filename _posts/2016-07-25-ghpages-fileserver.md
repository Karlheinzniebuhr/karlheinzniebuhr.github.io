---

layout: post
title:  "Github pages fileserver"
date:   2016-07-25
categories: [Technology]
tags: [Blogging, Technology]
banner_image: ghpages-fileserver.png
archived: true
---

Today's afternoon Experiment consisted of a simple file server which runs on top of gh-pages. 
[https://github.com/Karlheinzniebuhr/ghpages-fileserver](https://github.com/Karlheinzniebuhr/ghpages-fileserver)
<!--more-->
{% include image_full.html imageurl="/images/posts/ghpages-fileserver.png" title="" caption="" %}

Github is an awesome way to have virtually free hosting. The problem I noticed is that there was no easy way to "serve" files once you have them uploaded.
Inserting every Link manually in Markdown is a very time-consuming and boring task. There has to be an easier way. Luckily Jekyll supports static files [http://jekyllrb.com/docs/static-files/.](http://jekyllrb.com/docs/static-files/)

All I did was just loop over all files and filter out the ones contained in the /resources directory. Otherwise, irrelevant files of the blog would be displayed on the screen.  
<script src="https://gist.github.com/Karlheinzniebuhr/39570a0719971297fab8157ada2a55ef.js"></script>

This simple thing + some formatting and voila, we got a nice little file server running.  
For instructions on how to setup see the [Readme on Github.](https://github.com/Karlheinzniebuhr/ghpages-fileserver)   
Enjoy 🍻
