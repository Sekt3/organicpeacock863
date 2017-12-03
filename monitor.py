#!/usr/bin/python
from scapy.all import *
def printing(pkt):
 return str(pkt.show)

"""I don't remember what this was for, I think it was activated by access to a fake xmlrpc page. named .php but actually python cgi parsing requests. It was a neat way to find information on attackers sort of."""
 
sniff(filter='port not ssh and host not 127.0.0.1', prn=printing)
