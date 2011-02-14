#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import time

def genPayload():
	payload           = {}
	payload['data']   = {}
	payload['header'] = {}
	payload['header']['time']  = str(time.time())
	return payload

def auth( session, username, password ):
	payload = genPayload()

	payload['header']['sid']   = session
	payload['header']['class'] = "AUTH"
	payload['data']['uname']   = username 
	payload['data']['ident']   = password

	return payload

def autha( session, errors, status, message ):
	payload = genPayload()

	payload['header']['sid']    = session
	payload['header']['class']  = "AUTHA"
	payload['header']['errors'] = errors
	payload['header']['msg']    = message
	payload['data']['status']   = status

	return payload

def errora( session, errors, message ):
	payload = genPayload()

	payload['header']['sid']    = session
	payload['header']['class']  = "ERRORA"
	payload['header']['errors'] = errors
	payload['header']['msg']    = message

	return payload

