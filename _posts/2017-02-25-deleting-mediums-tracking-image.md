---
layout: post
title: "Deleting Medium's tracking Image"
date: 2017-02-25 09:06:59 +0000
categories: [Blog]
tags: [Blogging, Technology]
---

Recently I moved my blog away from Medium to be able to customize it. Luckily, Medium allows its users to be the owners of their content, which is why it is possible to export the content in a collection of HTML files and one XML file.
The only thing which stays on the medium servers are the images, though, which is not such a big problem normally as they display just fine within the post's themselves. Where the problem starts is when you use a plugin to extract the images, for a gallery or preview for example.
On [my blog](http://www.karlbooklover.com/blog/), I noticed, after importing the medium content, that on some posts the normal image showed up just fine, while on other ones there was an empty square. Initially, I thought that this was a problem with the plugin, I contacted customer support, and they responded.
> In your post content, there was an image, but that is tracking image (1 pixel image) of [medium.com](http://medium.com/).
>
> Please add this code to **Custom CSS** field in Content Views >> Settings page:
>
> ***img {display:none}***
>
> Best regards,

Oh, "tracking image", now that's interesting. It seems like Medium wants to know where the content is going after all. I didn't like the CSS option, though, because it would still be loaded from medium's servers. That's when I started deleting the tracking image HTML part in WordPress.
> <img src="https://medium.com/\_/stat?event=post.clientViewed&referrerSource=full\_rss&postId=ad649657d256" width="1" height="1" />

When you export your content, and before you import it to your new platform, just use an Editor like Atom and search for the above code in all files and replace it with an empty string --> "", that will solve the problem.
Cheers
Karl
