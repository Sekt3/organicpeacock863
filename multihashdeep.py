#!/usr/bin/env python

import os,sys,hashlib,platform

runningos = str(platform.system())
def run(file):
    infile = open(file, "rb")
    content = infile.read()
    infile.close()
    hashes("md5", content)
    hashes("sha1", content)
    hashes("sha256", content)
    hashes("sha512", content)


def hashes(type, content):
    try:
        if type == "md5":
            m=hashlib.md5(content)
        elif type == "sha1":
            m=hashlib.sha1(content)
        elif type == "sha256":
            m=hashlib.sha256(content)
        elif type == "sha512":
            m=hashlib.sha512(content)
        else:
            print "unknown type: "+str(type)
        print str(type)+": "+str(m.hexdigest())
    except UnboundLocalError:
        print "exiting... "
        exit()


def main():
 try: 
  if sys.argv[1] != None:
   inpt=sys.argv[1]
   print "--------- hashes for "+str(inpt)+" -------"
   for r, d, f in os.walk(str(inpt)):
	for i in r:
		for root, dir, files in os.walk(r):
			for fp in files:
				try:
				    test = len(root) - 1
                                    if runningos == "Linux":
					    if root[test] != "/":
                                                root=str(root)+"/"
				    elif runningos == "Windows":
                                            if root[test] != "\\":
                                                root=str(root)+"\\"
                                    fn=root+fp
                                    if runningos == "Linux":
                                            file=str(fn).replace(" ", "\ ")
                                    elif runningos == "Windows":
                                            file=str(fn)
                                    else:
                                        print "File grab issues, investigate."
                                        exit()
                                    print "~~~ "+str(file)+" ~~~"
				    run(file)
				except IOError:
				    print str(file)+" - failed to open"
				    pass
  else:
    print "Usage: python hashdeep.py {file or directory}"
 except:
	print "Usage: python hashdeep.py {file or directory}"

if __name__ == "__main__":
    main()
