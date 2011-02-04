#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

UsernameDatabase = {
	"paultag" : "DBAABD"
}

def getUserPassword(username):
	global UsernameDatabase;

	try:
		return UsernameDatabase[username]
	except KeyError as e:
		print "[log] User not found."
		KeyError("User not found")
