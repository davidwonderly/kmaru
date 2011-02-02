#!/usr/bin/env python

# OK. Gametime.

import kmaru.lcia

r_payload          = {}
r_payload['class'] = "auth"
r_payload['sid']   = 2
r_payload['time']  = 1234567890
r_payload['data']  = {}

r_payload['data']['uname'] = "tag"
r_payload['data']['ident'] = "ADBBDA"


r_ack = kmaru.lcia.xml_r(r_payload)
print r_ack;
