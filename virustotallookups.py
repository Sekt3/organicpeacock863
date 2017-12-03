import requests, time

apikey={get Yer Own}
for domain in open('dnslist','rb').readlines():
 if domain != "":
  if domain != "\n":
   a=requests.post("https://www.virustotal.com/vtapi/v2/url/scan",verify=False,data={"apikey":apikey,"url":str(domain).replace(" ","").replace("\n","")}).json()['permalink']
   print a
   open('/root/virustotallinks','a').write(str(a)+"\n")
   time.sleep(35)
   a=requests.post("https://www.virustotal.com/vtapi/v2/url/scan",verify=False,data={"apikey":apikey,"url":str(domain).replace(" ","").replace("\n","")+":7777"}).json()['permalink']
   print a
   open('/root/virustotallinks','a').write(str(a)+"\n")
   time.sleep(35)

