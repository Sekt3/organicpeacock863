#! /usr/bin/python
''' This is exactly what it looks like. But it served it's purpose. '''
import requests, json, sys, urllib
url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
print url
parameters = {'ip': str(sys.argv[1]), 'apikey': ''}
print parameters
response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
print response
response_dict = json.loads(response)
print response_dict
