#!/usr/bin/python
import sys, os
try:
 if sys.argv[1] != None:
  if isinstance(sys.argv[1],str) == True:
   if sys.argv[0] != "python":
    fileToZero=sys.argv[1]
   elif sys.argv[0] != os.path.basename(__file__):
    fileToZero=sys.argv[1]
   else:
    print "Usage: python filedestroy.py {filename}"
  else:
   print "Usage: python filedestroy.py {filename}"
 else:
  print "Usage: python filedestroy.py {filename}"
except:
 print "Usage: python filedestroy.py {filename}"
 exit()
with open(fileToZero,'ab') as f:
 count=int(len(open(fileToZero,'rb').read()))
 open(fileToZero,'wb').write("00".decode('hex'))
 for i in range(0,count):
  f.write('00'.decode('hex'))
os.remove(fileToZero)

