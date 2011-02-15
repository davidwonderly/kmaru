#!/usr/bin/env python

import unittest
import kmaru.api
import kmaru.lcia

class ApiTestCase(unittest.TestCase):
	def testAuthPayloadIsValid(self):
		sessionID = "0"
		username  = "paultag"
		password  = "testtickle"

		payload = kmaru.api.auth(sessionID,username,password)
		xml_payload = kmaru.lcia.xml_r(payload)
		print xml_payload
		payload_two = kmaru.lcia.readString(xml_payload)

		print "PI:  " + str(payload)
		print "PII: " + str(payload_two)

		assert payload == payload_two
		

if __name__ == "__main__":
    unittest.main() # run all tests

