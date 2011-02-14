#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.protocol_plugins

class auth:
	def answer(payload, protocol):
		print payload

	def request(payload, protocol):
		print payload
