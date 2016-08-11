---
layout: post
title:  "How to hide your IP when using Gmail"
date:   2015-10-12
permalink: /en/:year/:month/:day/:title/
tags: [security, gmail, networking, privacy]
banner_image: ip_test.png
---

I thought that Gmail always substituted the origin IP from our E-mail's. But this isn’t always the case.

I made some tests after noticing that E-mails send via Gmail from the Apple Mail application had my personal IP address in the header.  
<!--more-->
{% highlight text %}
Received: from [192.168.2.2](host-24-140.b8.cmm.com.py. [200.**.183.***])
        by smtp.gmail.com with ESMTPSA id 105sy7819552qgl.13.2015.10.12.13.16.52
        for <karl********@gmail.com>
        (version=TLSv1 cipher=ECDHE-RSA-RC4-SHA bits=128/128);
        Mon, 12 Oct 2015 13:16:53 -0700 (PDT)

{% endhighlight %}

Notice the
{% highlight text %}
Received: from [192.168.2.2](host-24-140.b8.cmm.com.py. [200.**.183.***])
{% endhighlight %}  
This metadata can be found in the header of the E-mail. You can easily check it out from the Gmail Web Client just by clicking on the button on the right side of the received E-mail and then on “show original” as shown in the Image (in German). Then search for the “Received:” field(s).  

![Image IP_test](https://raw.githubusercontent.com/Karlheinzniebuhr/karlheinzniebuhr.github.io/master/data/gmail_ip/ip_test.png)  

After this finding I tried again using the Web Client, apparently Gmail replaces the origin IP with their internal server’s IP just fine in this case. No client IP nor other client information shown.  
Notice that there can be multiple "Received from" fields and the order in which they appear is related to the servers involved in passing along your E-mail until it reaches its final destination.

{% highlight text %}
Delivered-To: karl*@gmail.com
Received: by 10.36.215.66 with SMTP id y63csp1646731itg;
        Mon, 12 Oct 2015 12:49:56 -0700 (PDT)
X-Received: by 10.31.149.86 with SMTP id x83mr17488958vkd.104.1444679396730;
        Mon, 12 Oct 2015 12:49:56 -0700 (PDT)
Return-Path: <elcanal*@gmail.com>
Received: from mail-vk0-x232.google.com (mail-vk0-x232.google.com. [2607:f8b0:400c:c05::232])
        by mx.google.com with ESMTPS id h62si4572036vkc.27.2015.10.12.12.49.56
        for <karl*@gmail.com>
        (version=TLSv1.2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Mon, 12 Oct 2015 12:49:56 -0700 (PDT)
Received-SPF: pass (google.com: domain of elcanal*@gmail.com designates 2607:f8b0:400c:c05::232 as permitted sender) client-ip=2607:f8b0:400c:c05::232;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of elcanal*@gmail.com designates 2607:f8b0:400c:c05::232 as permitted sender) smtp.mailfrom=elcanal*@gmail.com;
       dkim=pass header.i=@gmail.com;
       dmarc=pass (p=NONE dis=NONE) header.from=gmail.com
Received: by mail-vk0-x232.google.com with SMTP id w128so32211327vka.0
        for <karl*@gmail.com>; Mon, 12 Oct 2015 12:49:56 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20120113;
        h=mime-version:in-reply-to:references:date:message-id:subject:from:to
         :content-type;
        bh=OG2UrYUQdmCUqDpmwYXcgCfUCZtl1dhSDla5MYeq/Oc=;
        b=zK4xWYjHxcawzrE0oBXUPBCGqqnZJUcYRwqXh23PRKOo6dvjd0Jeisndnja1WOHFoH
         imj1n07CFd1O4PKX7x5YRUOzvWFKLalIBT/csGlyjoDjEzXLCZPbIHk+52cLfzixaT8T
         nBug+SwiS4ssTy5v7QQLQTy3obtsOixLGRAIwMaCQ9iJBNW6epiUigNJugBUADgp7nOK
         4ATiNotS8sHD+xRNi1xKtI5nN+2GCFjjxI5xGXQaGYuZYqk3GI5epJWQqYv7NXwGElJx
         5vxnoB5BZ3Dbo2wyTwt1APw4SdGhuowPYcg5YbYvM8PGBpQPwDIksoWP+s1JzI7ywVbg
         yzDw==
MIME-Version: 1.0
X-Received: by 10.31.141.130 with SMTP id p124mr17877289vkd.44.1444679396568;
 Mon, 12 Oct 2015 12:49:56 -0700 (PDT)
Received: by 10.31.149.11 with HTTP; Mon, 12 Oct 2015 12:49:56 -0700 (PDT)
In-Reply-To: <38A7606C-6E6B-4238-95E4-3C7ECEE8DE6F@gmail.com>
References: <38A7606C-6E6B-4238-95E4-3C7ECEE8DE6F@gmail.com>
Date: Mon, 12 Oct 2015 21:49:56 +0200
Message-ID: <CAG9DOV-skAuD=AT+t2VbJtGpn9b_SSnb3kKw9ivNMY03xMBDPA@mail.gmail.com>
Subject: Re: blablablabla
From: El canal de madara <elcanal*@gmail.com>
To: "karl (Karl)" <karl*@gmail.com>
Content-Type: multipart/alternative; boundary=001a11425a4e3f32340521eda2ee
{% endhighlight %}

Also using the Gmail Android application seems to be save.  

{% highlight text %}
MIME-Version: 1.0
Received: by 10.36.3.11 with HTTP; Mon, 12 Oct 2015 13:55:05 -0700 (PDT)
Received: by 10.36.3.11 with HTTP; Mon, 12 Oct 2015 13:55:05 -0700 (PDT)
Date: Mon, 12 Oct 2015 17:55:05 -0300
Delivered-To: karl***@gmail.com
Message-ID: <CAB1PxDQqFKhihLaIJWviGmEiqgh_JvtEhh3BiUys4_b8Fz97dQ@mail.gmail.com>
Subject: Ip test android
From: karl* <karl********@gmail.com>
To: karl* <karl********@gmail.com>
Content-Type: multipart/alternative; boundary=001a1145bb36566dcc0521ee8b37
{% endhighlight %}


#### Wrapping Up    
Depending on what method you use to send E-mails via Gmail, it can show your personal IP in the header, for example when using it via desktop applications. If you wan't to protect your personal IP address you should send your mail from the Web Client or make sure that mails sent via your mobile application are anonymised.  
