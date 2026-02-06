---
layout: post
title: "Collect Mikrotik RouterOS Logs with Rsyslog"
date: 2019-02-04 10:30:14 +0000
categories: ["Tech-blog"]
tags: ["mikrotik", "routeros"]
---

Logs are useful, I'd even say the most important thing for Sysadmins and Network Admins and often Developers also. So I'm surprised why I took so long to implement a central log collection for my network. I use Mikrotik which Operating System is called RouterOS. In RouterOS you go to System > Logging to configure remote logging.

First add (+) a new item to Actions

```
/system logging action add name="rsyslog" target=remote remote=192.168.2.1 remote-port=514;
```

Add a rule for every type of event you want to send to the remote logger.

```
system logging add topics=info action=rsyslog;
system logging add topics=error action=rsyslog;
system logging add topics=warning action=rsyslog;
system logging add topics=critical action=rsyslog;
```

The machine I'm using to collect the logs runs Rsyslog v8.   
 First, let's create a new logfile and give it the right permissions.

```
touch /var/log/mikrotik.log
chown syslog:adm /var/log/mikrotik.log
```

Then we need a config file, I name mine touch /etc/rsyslog.d/10-mikrotik.conf

Add this to the config file:

```
# Mikrotik Logs Conf
if ($fromhost-ip != "127.0.0.1" ) then /var/log/mikrotik.log
```

What this config does is it looks for all logs coming from other than the localhost, which in our case are the Mikrotik routers.  
Restart Rsyslog and you should be able to see the first logs coming in.

```
service restart rsyslog
tail -f /var/log/mikrotik.log
```
