#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.module

def answer(args):
	payload  = args[0]
	protocol = args[1]

	print payload

def request(args):
	payload  = args[0]
	protocol = args[1]

	print payload


kmaru.module.addModule(   "AUTH", answer  );
kmaru.module.addModule(  "AUTHA", request );

