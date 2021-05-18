---
layout: post
title: ObliqueRAT
---

### ObliqueRAT
Maldoc
   * Document file(docx) dropped the exe auto open -> deobfuscate -> write to file
   * Ole file contains Stomped code [for detail](https://medium.com/walmartglobaltech/vba-stomping-advanced-maldoc-techniques-612c484ab278)
   * Contains suspicious  strings [for details](https://github.com/vidyasagarpanjri/vidyasagarpanjri.github.io/blob/master/_posts/data/obliqueRAT/README.md)

Deobfuscate Maldoc:
   * use oledump to dump the data
   * Macros/UserForm1/o contians the obfuscated data for exe 
   * deobfuscate split with 'O' -> convet the int values to char -> write to file

[deobfu.py](https://github.com/vidyasagarpanjri/vidyasagarpanjri.github.io/blob/master/_posts/data/obliqueRAT/deobfu.py)



