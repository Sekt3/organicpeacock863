#!/usr/bin/python
from netaddr import IPNetwork
import socket, os

list=map(str, str(raw_input("Add comma seperated ip ranges: ")).split(","))
for i in list:
  for ip in IPNetwork(i):
   open('iplist-%s.log' % i.replace('/',''), 'a').write(str(ip)+","+str(socket.gethostbyaddr(str(ip))[0])+"\n")

