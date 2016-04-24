from shutil import copyfile
import filecmp
while 1:
	if filecmp.cmp ("/tmp/shairport-sync/image", "~/metadata_webserver/shairport-sync-metadata-webserver/image") == True:
		continue
	else:
		shutil.copyfile("/tmp/shairport-sync/image", "~/metadata_webserver/shairport-sync-metadata-webserver/image")