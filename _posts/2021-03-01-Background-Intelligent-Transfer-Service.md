---
layout: post
title: Background Intelligent Transfer Service
---

Next you can update your site name, avatar and other options using the _config.yml file in the root of your repository (shown below).

![_config.yml]({{ site.baseurl }}/images/config.png)

##  Background Intelligent Transfer Service

As the name suggest the BITS is a feature in windows, which start downloading the windows updates when there is no or minimal network activity is observered.
In short it uses the free bandwidth to downlaod software updates.

How to download the data from remote server:
    There is a powershell command utility available :
    Start-BitsTransfer -Source "https://example.com/file.zip" -Destination "C:\file.zip" -DisplayName "myDownloadJob"

#### There are many applications which uses this feature to update itself liek Firefox, Chrome etc.

Malicious use of BITS:
-
    1. Win32/StealthFalcon backdoor as reported by ESET researchers.
    2. Zlob.Q trojan as reported by secureworks.
    3. UBoatRAT as reported by paloaltonetworks.
    4. Older Version of bazarLoad alos used this feature.

There are primarily many advantages of BITS for malware:
-

   * Defense Evasion:  T1197, https://attack.mitre.org/techniques/T1197, Security Operations often do not analyse this traffic as it is mostly use by windows.
   * Persistance :  T1197, https://attack.mitre.org/techniques/T1197, BITS can be configured to keep downloading the paylaod after certain period of time.
   * Execution : T1053, https://attack.mitre.org/techniques/T1053, after download the payload BITS can execute the binary.
   * Command and Control: T1008, https://attack.mitre.org/techniques/T1008, Fallback Channel, 
   * Exfiltration: T1029, https://attack.mitre.org/techniques/T1029, we can periodically send the data to remote server.



Reference:
-
    * https://unit42.paloaltonetworks.com/unit42-uboatrat-navigates-east-asia/
    * https://www.secureworks.com/blog/malware-lingers-with-bits
    * https://attack.mitre.org/
