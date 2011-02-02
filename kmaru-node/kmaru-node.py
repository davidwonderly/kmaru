#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import kmaru.lcia

r_payload           = {}
r_payload['header'] = {}

r_payload['header']['class'] = "auth"
r_payload['header']['sid']   = 2
r_payload['header']['time']  = 1234567890

r_payload['data']  = {}

r_payload['data']['uname'] = "tag"
r_payload['data']['ident'] = "ADBBDA"


r_ack = kmaru.lcia.xml_r(r_payload)
print r_ack;
