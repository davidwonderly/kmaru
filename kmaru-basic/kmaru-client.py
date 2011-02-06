#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.client
import kmaru.hil

port    = 2017
host    = "localhost"

uname = kmaru.hil.query("Username")
ident = kmaru.hil.query("Password")

kmaru.client.runssl(
	port,
	host,
	uname,
	ident
)

