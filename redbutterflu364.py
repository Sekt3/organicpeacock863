#!/usr/bin/python
import sys, os, requests
def ghost(dat):
    data={"text": str(open(dat, 'rb').read().encode('base64')), "expire": "-1", "lang":"text"}
#    print data
# There is a good chance if it didn't work, you had too much data to post
    response=requests.post("https://ghostbin.com/paste/new", data=data, verify=False)
#    print response.text
    return response.url

if __name__ == '__main__':
    try:
        print ghost(sys.argv[1])
    except:
#	print sys.exc_info()
        print "Usage:\r\nScript.py {filename}\r\n-----------------------\r\nThis is available as both full location and location compared to your current location"
    exit()
