#!/usr/bin/python
import os
import time
from shutil import copyfile
x = 1
while True:
        if os.path.exists("/tmp/shairport-sync/image") == True:
                copyfile('/tmp/shairport-sync/image', '/root/shairport-sync-metadata-webserver/image')
                tmpimage = os.path.getsize("/tmp/shairport-sync/image")
                rootimage = os.path.getsize("/root/shairport-sync-metadata-webserver/image")
                while True:
                        if (tmpimage == rootimage) == True:
                                time.sleep(1)
                                print("Now playing album art equals to the one on webserver.")
                                x = x + 1
                                while x == 10:
                                        os.system("./b64_to_image.py image")
                                        if os.path.exists("/tmp/shairport-sync/artist") == True:
                                                copyfile('/tmp/shairport-sync/artist', '/root/shairport-sync-metadata-webserver/artist')
                                                copyfile('/tmp/shairport-sync/album', '/root/shairport-sync-metadata-webserver/album')
                                                copyfile('/tmp/shairport-sync/title', '/root/shairport-sync-metadata-webserver/title')
                                        x = 1
                                break
                        else:
                                copyfile('/tmp/shairport-sync/image', '/root/shairport-sync-metadata-webserver/image')
                                print("Copying image from tmp to webserver...")
                                time.sleep(1)
                                print("Converting base64 to image...")
                                os.system("./b64_to_image.py image")
                                print("Copying metadata from tmp to webserver...")
                                if os.path.exists("/tmp/shairport-sync/artist") == True:
                                        copyfile('/tmp/shairport-sync/artist', '/root/shairport-sync-metadata-webserver/artist')
                                        copyfile('/tmp/shairport-sync/album', '/root/shairport-sync-metadata-webserver/album')
                                        copyfile('/tmp/shairport-sync/title', '/root/shairport-sync-metadata-webserver/title')
                                break
        else:
                print("Music is not playing.")
                os.system("rm album")
                os.system("rm artist")
                os.system("rm title")
                time.sleep(5)
                continue