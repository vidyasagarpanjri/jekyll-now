---
layout: post
title: Creating filter template for apimonitor
---

### Tools used
  
  API Monitor v2 (Alpha-r13) - x86 32-bit     [Download as per your OS](http://www.rohitab.com/downloads)
  peframe   [DOwnload and install from here](https://github.com/guelfoweb/peframe)
  
 
 ### Problem statement  
 During the Dynamic analysis of any file in window we often(we = me) use apimoitor from rohitab. It is a very handy tool, we can monitor the apicalls and argumets passed. 
 But problem I face is to quicly find out what APIs to monitor how quckly we can check/select those APIs.
 
 As I wrote this script specily for malware analysis, I used peframe by [@guelfoweb](https://twitter.com/guelfoweb) to get possible APIs.
### peframe result
[![asciicast](https://asciinema.org/a/pRG8MROJMfcptYBrbXjWmLwOX.svg)](https://asciinema.org/a/pRG8MROJMfcptYBrbXjWmLwOX)

 I have modified the the peframe little bit to get APIs along with their libraries names, something like "KERNEL32.TerminateProcess".
    update "peframe/peframe/modules/apialert.py" file
      replace line '''alerts.append(imp.name.decode('ascii'))''' with '''alerts.append(str(lib.dll)[2:-5]+"."+imp.name.decode('ascii'))'''
### update peframe apialert.py module
[![asciicast](https://asciinema.org/a/X9ccxQXWcXxVKMjxNo76vMrci.svg)](https://asciinema.org/a/X9ccxQXWcXxVKMjxNo76vMrci)

now using the script we can create the filter xml for apimonitr.
### demo
[![asciicast](https://asciinema.org/a/u7m3w4SYv1Am8by7MHOLZzoW5.svg)](https://asciinema.org/a/u7m3w4SYv1Am8by7MHOLZzoW5)

now just load xml file creaed the file see the magic.
