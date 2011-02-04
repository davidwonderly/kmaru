#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.auth

def authProcessor(ServerMain, payload):

	try:
		achal = kmaru.auth.getUserPassword(payload['data']['uname'])

	except KeyError as e:
		print "[log] User not found."

	paylard = {}

	if achal == payload['data']['ident']:
		print "[log] User's password matches."
		paylard = kmaru.api.autha(
			payload['header']['sid'], # session
			"OK",                     # status
			0,                        # errors
			"Logged in!"              # Human readable
		)
	else:
		print "[log] User's password does not match."
		paylard = kmaru.api.autha(
			payload['header']['sid'], # session
			"FAIL",                   # status
			-1,                       # errors
			"Failed to login!"        # Human readable
		)

	ServerMain.send_a(paylard)
