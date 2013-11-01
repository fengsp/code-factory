# -*- coding: utf-8 -*-

import os
import urllib
from urlparse import urlsplit
from pprint import pprint

from pyPdf import PdfFileReader
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS


def pdf_meta(filepath):
    pdf_file = PdfFileReader(file(filepath, 'rb'))
    info = pdf_file.getDocumentInfo()
    print '[*] PDF MetaData For: ' + str(filepath)
    for meta_item in info:
        print '[+] ' + str(meta_item) + ':' + str(info[meta_item])


def img_find(url):
    print '[+] Finding images on ' + url
    content = urllib.urlopen(url).read()
    soup = BeautifulSoup(content)
    img_tags = soup.findAll('img')
    return img_tags


def img_down(img_tag):
    try:
        print '[+] Downloading image...'
        img_src = img_tag['src']
        img_filename = os.path.basename(urlsplit(img_src)[2])
        urllib.urlretrieve(img_src, img_filename)
        return img_filename
    except:
        return ''


def img_meta(filepath):
    exif_data = {}
    img_file = Image.open(filepath)
    info = img_file._getexif()
    if info:
        for (tag, value) in info.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
        print '[*] MetaData For ' + filepath
        pprint(exif_data)


if __name__ == "__main__":
    pdf_meta('/Users/fsp/Documents/EBooks/通讯录-2012.10.pdf')

    img_tags = img_find('http://ezine.oupeng.com/list/show.do?cid=19&p=1&trace=22')
    for img_tag in img_tags:
        img_filename = img_down(img_tag)
        img_meta(img_filename)
