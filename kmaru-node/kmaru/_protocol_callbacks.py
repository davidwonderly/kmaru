#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.auth
import kmaru.globals

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
			0,                        # status
			kmaru.globals.OK,         # errors
			"Logged in!"              # Human readable
		)
	else:
		print "[log] User's password does not match."
		paylard = kmaru.api.autha(
			payload['header']['sid'], # session
			-1,                       # status
			kmaru.globals.FAIL,       # errors
			"Failed to login!"        # Human readable
		)
	ServerMain.send_a(paylard)
