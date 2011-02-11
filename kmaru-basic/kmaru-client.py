#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.client
import kmaru.hil

port    = 2017
host    = "localhost"

uname = "paultag" # kmaru.hil.query("Username")
ident = "hey"     # kmaru.hil.query("Password")

kmaru.client.runssl(
	port,
	host,
	uname,
	ident
)

