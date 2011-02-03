#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.server
import twisted.internet.error

port = 2017

print "We're running kmaru on port " + str(port)

try:
	kmaru.server.runssl(
		port,
		"ssl-keys/server.key",
		"ssl-keys/server.crt"
	)
except twisted.internet.error.CannotListenError as e:
	print "Failure to load server. Error follows."
	print ""
	print e
	print ""

