---
layout: post
title: "How to disable Samsung's annoying Bloatware"
date: 2018-09-25 09:40:23 +0000
categories: [Technology]
---

If there is something that infuriates me it is bloatware that cannot be disabled. I happened to get a notification every few minutes from "Samsung Experience Service" for the last couple of weeks.

There was no way to disable that shit. I found online forums full of complaints. Good job Samsung you are alienating your clients.

![](/assets/images/samsung-bloatware.jpg)

Ok so let's get rid of this. The first step is to [download ADB](https://dl.google.com/android/repository/platform-tools-latest-windows.zip).

Open the command prompt and switching to the directory where **adb.exe** is located.

Make sure your Samsung is connected to the PC and click on **Allow USB Debugging.** You find a detailed guide [here](https://www.xda-developers.com/install-adb-windows-macos-linux/).

Once ready, execute this command:

```
./adb.exe shell pm uninstall -k --user 0 com.samsung.android.mobileservice
```

![](/assets/images/image.png)

If you get **Success** in the command prompt, the notifications should no longer appear.

Cheers

Ah, and by the way, you can check what other bloat and spyware there is to uninstall.

```
./adb.exe shell pm list packages
```

If you use cygwin you can grep all samsung apps just to see how much bloat action there is really going on.

```
./adb.exe shell pm list packages | grep samsung
```

Count Samung Packages

```
./adb.exe shell pm list packages | grep samsung | wc -l
```

My s7 with Oreo has 121 Samsung packages. Are they all necessary? Probably not.
