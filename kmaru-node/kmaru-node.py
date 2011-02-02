#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.lcia
import kmaru.api

try:
	payload = kmaru.api.auth("1","paultag","ADBBDA")
	print kmaru.lcia.xml_r(payload)

	payload = kmaru.api.autha( "1", "0", "OK", "Logged in Fine!" )
	print kmaru.lcia.xml_a(payload)

except KeyError as e:
	print "Error sending auth! " + str(e)
