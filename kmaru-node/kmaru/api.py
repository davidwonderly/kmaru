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


def autha( session, errors, status, message ):
	payload           = {}
	payload['data']   = {}
	payload['header'] = {}

	payload['header']['sid']    = session
	payload['header']['time']   = time.time()
	payload['header']['class']  = "AUTHA"
	payload['header']['errors'] = errors
	payload['header']['msg']    = message

	payload['data']['status']   = status
	return payload

def errora( session, errors, message ):
	payload           = {}
	payload['data']   = {}
	payload['header'] = {}

	payload['header']['sid']    = session
	payload['header']['time']   = time.time()
	payload['header']['class']  = "ERRORA"
	payload['header']['errors'] = errors
	payload['header']['msg']    = message

	return payload
