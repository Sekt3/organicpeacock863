#!/usr/bin/python
import requests
a=requests.get('https://www.iocbucket.com/feeds/rss2/yara/latestten', verify=False)
for i in a.text.splitlines():
 if "==</description>" in i:
  print i.replace('<description>', '').replace('</description>', '').decode('base64').decode('zlib')
  print "--------------------"
print
print "||||||||||||||||||||||||||||||"
print
a=requests.get('https://www.iocbucket.com/feeds/rss2/openioc/1.0/latestten', verify=False)
for i in a.text.splitlines():
 if "==</description>" in i:
  print i.replace('<description>', '').replace('</description>', '').decode('base64').decode('zlib')
  print "--------------------"
print
print "||||||||||||||||||||||||||||||"
print
a=requests.get('https://www.iocbucket.com/feeds/rss2/openioc/1.1/latestten', verify=False)
for i in a.text.splitlines():
 if "==</description>" in i:
  print i.replace('<description>', '').replace('</description>', '').decode('base64').decode('zlib')
  print "--------------------"
print
print "||||||||||||||||||||||||||||||"
print

