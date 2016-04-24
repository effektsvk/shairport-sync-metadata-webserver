#!/usr/bin/python
import os
import time
from shutil import copyfile
while True:
        if (os.path.getsize("/tmp/shairport-sync/image") == os.path.getsize("/root/metadata_webserver/shairport-sync-metadata-webserver/image")) == True:
                time.sleep( 5 )
                print("Now playing album art equals to the one on webserver.")
                continue
        else:
                copyfile('/tmp/shairport-sync/image', '/root/metadata_webserver/shairport-sync-metadata-webserver/image')
                print("Copying from tmp to webserver...")
                continue