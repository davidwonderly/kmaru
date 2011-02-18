#!/usr/bin/env python

import unittest
import kmaru.auth

GoodUser = {
	"uname" : "paultag",
	"idet"  : "heybabyhay"
}

BadUser = {
	"uname" : "joeshmo",
	"idet"  : "letmein"
}

class AuthTestCase(unittest.TestCase):
	def setUp(self):
		global GoodUser
		kmaru.auth.UsernameDatabase[GoodUser['uname']] = GoodUser['idet']
		print "Added user " + GoodUser['uname'] + " with password of " + GoodUser['idet']

	def testAuthGood(self):
		print "Test Auth Good"
		global GoodUser
		uname = GoodUser['uname']
		idet  = GoodUser['idet']
		print "Authing with: ", uname, idet
		assert kmaru.auth.validUser(uname,idet)

	def testAuthBad(self):
		print "Test Auth Bad"
		global GoodUser
		uname = GoodUser['uname']
		idet  = GoodUser['idet'] + "FROBERNATE"
		print "Authing with: ", uname, idet
		assert kmaru.auth.validUser(uname,idet) == False

	def testNoexistUser(self):
		print "Testing fake user"
		global GoodUser
		uname = GoodUser['uname'] + "xkcdrules"
		idet  = GoodUser['idet']
		print "Authing with: ", uname, idet
		try:
			kmaru.auth.validUser(uname,idet)
			assert False
		except KeyError as e:
			pass

if __name__ == "__main__":
    unittest.main() # run all tests

