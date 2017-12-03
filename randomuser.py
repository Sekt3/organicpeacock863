#!/usr/bin/python2.7
import requests, time, random
def dataFromApi():
	#get data
	data=requests.get('http://randomuser.me/api',verify=False).json()['results']
	# print data
	return data
def useData(data):
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
def dataService():
	data=dataFromApi()
	useData(data)
	time.sleep(random.randrange(45,300))
	dataService()
dataService()

