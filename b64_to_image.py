__author__ = 'JHealy'
from sys import argv, exit
import os
import base64
import imghdr

# This script converts base64 encoded image data to an image file of the appropriate type.
# It's kind of quick and dirty, not entirely bullet proof, but this is utility not a library.
# Could be improved by allowing batch conversions and wrapping the file reads/writes in try/except blocks
#
# Arguments: <filename> : a single file that contains the base64 encoded image data.
#
# Result: A new image file of the appropriate type called <filename>_converted.{png, gif, jpg, etc) in the same
#         folder as the source image


b64_data = ''

# Crap out if the user has called the script incorrectly
if len(argv) != 2:
    exit("Wrong number of arguments.  This script accepts a single argument.\nUsage: b64_to_image.py source_file")

# Split the command line to get the path and base file name (no extension) so we know what to call the new image file
command, file_path = argv
path_name, file_name = os.path.split(argv[1])
file_base_name = os.path.splitext(file_name)[0]

if path_name == '':
    path_name = '.'

# Open the source file and read in the base64 encoded data
try:
    source = open(file_name, 'r')
except IOError:
    print ("Unable to open {}.  Are you sure it's there?".format(file_name))
    exit()
else:
    b64_data = source.read()
    source.close()

# Convert the base64 data back to regular binary image data and figure out the image type (png, gif, jpg, etc)
image_data = base64.b64decode(b64_data)
image_type = imghdr.what('', image_data)

# Create the image file and tell the user about it
destination_file_name = path_name + '/' + file_base_name + '_converted.' + image_type
try:
    destination = open(destination_file_name, 'wb')
except IOError:
    print ("Unable to create image file. You might not have permission to create a file in this location.")
    exit()
else:
    destination.write(image_data)
    destination.close()
    print ("New image file: {}".format(destination_file_name))


