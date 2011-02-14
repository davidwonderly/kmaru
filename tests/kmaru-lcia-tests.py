#!/usr/bin/env python

import unittest
import kmaru.lcia

r_class_test_payload = {
	"header" : {
		"class" : "TEST",
		"sid"   : "-1",
		"time"  : "123456789",
	},
	"data"    : {
		"foobar" : "barbaz"
	}
}

a_class_test_payload = {
	"header" : {
		"class" : "TEST",
		"sid"   : "-1",
		"time"  : "123456789",
		"errors": "0",
		"msg"   : "Hello, World!"
	},
	"data"    : {
		"foobar" : "barbaz"
	}
}

class LicaTestCase(unittest.TestCase):
	def testRSeries(self):
		print ""
		print "R Series Tests"
		print ""

		global r_class_test_payload
		payload = r_class_test_payload

		xml_payload = kmaru.lcia.xml_r(payload)
		print xml_payload

		payload_two = kmaru.lcia.readString(xml_payload)

		print "PII: " + str(payload_two)
		print "PI:  " + str(payload)

		assert payload == payload_two

	def testASeries(self):
		print ""
		print "A Series Tests"
		print ""

		global a_class_test_payload
		payload = a_class_test_payload

		xml_payload = kmaru.lcia.xml_a(payload)
		print xml_payload

		payload_two = kmaru.lcia.readString(xml_payload)

		print "PII: " + str(payload_two)
		print "PI:  " + str(payload)

		assert payload == payload_two


if __name__ == "__main__":
    unittest.main() # run all tests

