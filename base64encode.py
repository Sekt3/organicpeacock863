#!/usr/bin/python
import requests,os,sys
if sys.argv[1] != None:
 try:
  print requests.post("https://ghostbin.com/paste/new",data={"text": open(str(sys.argv[1]), 'rb').read().encode('base64'),"expire":"-1","lang":"text"},verify=False).url
 except:
  print "Usage:\r\nbase64Encode.py {filename}\r\n-----------------------\r\nThis is available as both full location and location compared to your current location"
