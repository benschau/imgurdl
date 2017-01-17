#!/usr/bin/env python2.7

"""
Given an imgur link, download all the images in that gallery and pack it into a nice directory.
"""

from imgurpython import ImgurClient
import sys, os
import urllib
import getopt
import argparse

from client import Client

absclient = Client()
client = ImgurClient(absclient.id, absclient.secret)

# TODO: parse commandline args -> -c compress -t custom_title -i id-only
# get link from user (via argument)
parser = argparse.ArgumentParser(prog='imgurdl')
parser.add_argument('link')
parser.add_argument('-c', '--compress', action='store_true', help="compress downloaded gallery")
parser.add_argument('-t', '--title', nargs='?', help="rename downloaded gallery")
parser.add_argument('-i', '--id-only', nargs='?', help="input gallery id instead of whole link")

# TODO: If given a link, use the link. If given an ID, use the ID. Don't allow a user to give both arguments.
args = parser.parse_args()

link = args.link

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
