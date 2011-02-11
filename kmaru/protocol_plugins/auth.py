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

#kmaru.protocol_plugins.kmaru_callbacks['AUTHA'] = auth
kmaru.protocol_plugins.loadCallback("AUTH", auth)  #kmaru_callbacks['AUTH']  = auth
