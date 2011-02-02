#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import time

def auth( session, username, password ):
	payload           = {}
	payload['data']   = {}
	payload['header'] = {}
	payload['header']['sid']   = session
	payload['header']['time']  = time.time()
	payload['header']['class'] = "AUTH"
	payload['data']['uname']   = username 
	payload['data']['ident']   = password
	return payload
