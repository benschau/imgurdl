#!/usr/bin/env python2.7

"""
 imgurdl - Given an imgur gallery id, download all the images in that gallery and pack it into a nice directory.
"""

from imgurpython import ImgurClient
import sys, os
import urllib
import getopt
import argparse

# import helper
from client import Client

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='imgurdl')
    parser.add_argument('id')
    parser.add_argument('-c', '--compress', action='store_true', help="compress downloaded gallery")
    parser.add_argument('-t', '--title', nargs=1, help="rename downloaded gallery")
    parser.add_argument('-cp', '--credpath', nargs=1, help="define custom credential path")

    args = parser.parse_args()

    absclient = Client(args.credpath)
    client = absclient.client

    album_id = args.id

    album = client.get_album(album_id)
    album_title = args.title[0] if args.title[0] else album.title[0]

    if not os.path.exists(album_title):
        os.mkdir(album_title)

    os.chdir(album_title)

    album_images = client.get_album_images(album_id)
    for image in album_images:
        image_title = image.link[(image.link.rindex('/') + 1):]
        print('\t{0}: {1}'.format(image_title, image.link))
        urllib.urlretrieve(image.link, image_title) 

    os.chdir('../')
