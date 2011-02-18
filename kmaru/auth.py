#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

UsernameDatabase = {
	"paultag" : "hey"
}

def validUser(username, password):
	if getUserPassword(username) == password:
		return True
	else:
		return False

def getUserPassword(username):
	global UsernameDatabase;

	try:
		return UsernameDatabase[username]
	except KeyError as e:
		print "[log] User not found."
		raise
