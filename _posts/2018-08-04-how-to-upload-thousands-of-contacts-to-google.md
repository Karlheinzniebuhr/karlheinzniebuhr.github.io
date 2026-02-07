---
layout: post
title: "How to upload thousands of contacts to Google"
date: 2018-08-04 11:26:35 +0000
categories: [Technology]
---

Today a colleague asked me for help. The boss asked him to type in about 6000 registers of Name/Phone number on to Google Contacts. I thought, "there must be a better way" (borrowed that one from Raymond Hettinger).

Pre-processing

First things first, I deleted all the unnecessary columns from the spreadsheet. Then it was as simple as doing an export to CSV in LibreOffice Calc.

Next step, adding the right column names in the first row so that it coincides with the standard Google uses. In this case, I used: **Name, Phone.**

One problem remained though, I had to add a zero to the phone number prefix.

981xxxxxx had to be 0981xxxxxx

Time for some regular expressions

I used my favorite online regex editor to get my regex right. Back to notepad++

![](/assets/images/image.png)

EASY PEASY!

Just one more step, I had to split the file in two because Google threw an error as it supports only about 3000 contacts in one import.

Finally, I was able to upload all 6K contacts to <https://contacts.google.com/>
