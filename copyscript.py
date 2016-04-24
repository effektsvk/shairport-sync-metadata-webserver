#!/usr/bin/python
import os
import time
from shutil import copyfile
x = 1
while True:
        if os.path.exists("/tmp/shairport-sync/image") == True:
                copyfile('/tmp/shairport-sync/image', '/root/shairport-sync-metadata-webserver/image')
                while True:
                        if (os.path.getsize("/tmp/shairport-sync/image") == os.path.getsize("/root/shairport-sync-metadata-webserver/image")) == True:
                                time.sleep( 5 )
                                print("Now playing album art equals to the one on webserver.")
                                x = x + 1
                                while x == 5:
                                        os.system("./b64_to_image.py image")
                                        x = 1
                                break
                        else:
                                copyfile('/tmp/shairport-sync/image', '/root/shairport-sync-metadata-webserver/image')
                                print("Copying from tmp to webserver...")
                                time.sleep( 2 )
                                print("Converting base64 to image...")
                                os.system("./b64_to_image.py image")
                                break
        else:
                print("Music is not playing.")
                time.sleep( 10 )
                continue