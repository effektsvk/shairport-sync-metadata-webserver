Autorun of shairport-sync-metadata-reader

http://stackoverflow.com/questions/16823361/how-can-i-run-a-command-at-boot

---

Autorun of http-server

```
#!/usr/bin/python
import os

os.chdir("/root/shairport-sync-metadata-webserver")
os.system("http-server")
```

---

Autorun of copyscript.py

```
#!/bin/bash
cd /root/shairport-sync-metadata-webserver/
python copyscript.py
```