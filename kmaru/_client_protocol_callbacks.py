#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.globals

def authAnswerProcessor(ClientMain, paylard):
	if paylard['data']['status'] == kmaru.globals.FAIL:
		print "Failed to login."

	if paylard['data']['status'] == kmaru.globals.OK:
		print "Logged in well!"
