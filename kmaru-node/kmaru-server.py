#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.server
import twisted.internet.error

port    = 2017

keydir  = "./ssl-keys"
keyfile = "server.key"
crtfile = "server.crt"

print "We're running kmaru on port " + str(port)
print " Searching for SSL keys in: " + keydir + "/"
print "  ( looking for both " + keyfile + " and " + crtfile + " )"

try:
	kmaru.server.runssl(
		port,
		keydir + "/" + keyfile,
		keydir + "/" + crtfile
	)
except twisted.internet.error.CannotListenError as e:
	print "Failure to load server. Error follows."
	print ""
	print e
	print ""

