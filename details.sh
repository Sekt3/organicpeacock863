#!/bin/bash
'''Used as blog example'''
curl http://0daz.io/useful.log > useful.log 2>/dev/null; cat useful.log |awk '{print $1}' |sort |uniq -d|for n in `grep -iv 000webhostapp`; do grep -i $n useful.log > /tmp/lol; for i in `cat /tmp/lol`; do echo $i; whois $i|grep -i "cidr\|netname\|route\|OriginAS"; done; done > /var/www/html/details.log
mv /tmp/lol /var/www/html/listofdomainswithduplicates.log
