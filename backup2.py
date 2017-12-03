#! /usr/bin/python
import cgi, os, sys
''' This was made a while back to accomedate a webpage designed from data pulled from multiple hosts performing constant checks of dns resolution from multiple threat actors using dynamic dns changing routines'''


# To accomedate pagination that doesn't exist
nope="null"

#Define Threat Actor Domains
TA={"Threat Actor 1":(!LIST OF DOMAINS HERE!), "Threat Actor 2": (!Only a single domain here!, nope), "Threat Actor 3": (!LIST OF DOMAINS HERE!")}


#print page headers
print "Content-Type: text/html"
print 
print """<html><head><title>Real Time Threat Actor Domain Monitoring</title><meta http-equiv="refresh" content="30"></head><body bgcolor="black">
<center>
<a href="./ips-earliest.csv" >Latest CSV</a> | <a href="./iplist.lst"> Latest ip list</a> | <a href="./iplist-TA1.lst">IPs TA1</a> | <a href="./iplist-TA2.lst">IPs TA2</a> | <a href="./iplist-TA3.lst">IPs TA3</a>
</center><br><p>"""


# this really should be more for loops, but for now just copy this next section and change the 0 in this part "TA.keys()[0]"  to the numerical equivilent for the TA field. Such as 0=ta1, 1=ta2, 2=ta3...

# table
print """<br><table border="1" bgcolor="red" cellpadding="1" align="left">"""

# Copy This section
# TA1
print """<tr><td colspan=2><center>%s</center></td></tr>""" % str(TA.keys()[0])

#don't copy this one
print "<tr><td>Domain</td><td>Current IP</td></tr>"

#copy this section
for i in TA[str(TA.keys()[0])]:
  b=open('/shared/%s.log' % i, 'r').readlines()[-1].split(' ')[0]
  c=open('/shared/%s.log' % i, 'r').readlines()[-1].split(' ')[3]
  print "<tr>"
  print "<td>"+b, "<td>"+c
  print "</tr>"
#stop copying. 


# TA2 For some reason TA2 and TA3 are switching places in the list
print """<tr><td colspan=2><center>%s</center></td></tr>""" % str(TA.keys()[2])

for i in TA[str(TA.keys()[2])]:
  b=open('/shared/%s.log' % i, 'r').readlines()[-1].split(' ')[0]
  c=open('/shared/%s.log' % i, 'r').readlines()[-1].split(' ')[3]
  print "<tr>"
  print "<td>"+b, "<td>"+c
  print "</tr>"


#TA3 For some reason TA2 and TA3 are switching places in the list
print """<tr><td colspan=2><center>%s</center></td></tr>""" % str(TA.keys()[1])

for i in TA[str(TA.keys()[1])]:
  b=open('/shared/%s.log' % i, 'r').readlines()[-1].split(' ')[0]
  c=open('/shared/%s.log' % i, 'r').readlines()[-1].split(' ')[3]
  print "<tr>"
  print "<td>"+b, "<td>"+c
  print "</tr>"


# Paste Coppied section above this line. 
print "</body>"
print "</html>"
