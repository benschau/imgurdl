"""
Given an imgur link, download all the images in that gallery and pack it into a nice directory.
"""

from imgurpython import ImgurClient
import sys, os
import urllib
import getopt

# TODO: retrieve client_id and client_secret from a file somewhere.
client_id = 'ea0c50e04abfe9f'
client_secret = 'c44ae624290b662ff377e992508326048f6e5cb7'

client = ImgurClient(client_id, client_secret)

# TODO: getopt -> -c compress -t custom_title -i id-only
# get link from user (via argument)
link = str(sys.argv[1])

# Strip everything in front of imgur
ind = link.find('imgur')
if not (ind == -1):
    link = link[ind:] 

# take the album's id, e.g the random string at the end of imgur.com/gallery
index = link.rindex('/') + 1
album_id = link[index:]

album = client.get_album(album_id)
album_title = album.title

# make a directory and move into it
if not os.path.exists(album_title):
    os.mkdir(album_title)

os.chdir(album_title)

# put all the images into the gallery.
album_images = client.get_album_images(album_id)
for image in album_images:
    image_title = image.link[(image.link.rindex('/') + 1):]
    print('\t{0}: {1}'.format(image_title, image.link))
    urllib.urlretrieve(image.link, image_title) 

os.chdir('../')