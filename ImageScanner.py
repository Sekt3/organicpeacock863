#! /usr/bin/python
import os,sys,string
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    print ret

def get_png(fn):
    ret = {}
    i = Image.open(fn)
    info1 = i.info
    info2 = i._getexif()
    for tag, value in info2.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    print ret
    print info1


if len(sys.argv) == 2:
 for root, dirs, files in os.walk(str(sys.argv[1])):
        for fp in files:
                try:
                        fn1=root+fp
                        if ".jpg" or ".gif" in fn1:
                                print fp
                                get_exif(fn1)
                                print
                                print
                                print
                                """for spacing purposes"""
                        elif ".png" in fnl:
                                print fp
                                get_png(fn1)
                                print
                                print
                                print
                                """for spacing purposes"""

                        else:
                                print "File %s does not appear to be a picture file" % fp
                except:
                        pass
else:
 print "Usage: ./Mara's_Image_Scanner.py {file or file directory} "

