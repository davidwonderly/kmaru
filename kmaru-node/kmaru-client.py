#!/usr/bin/env python
#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

from twisted.internet import ssl, reactor
from twisted.internet.protocol import ClientFactory, Protocol

import kmaru.api
import kmaru.lcia

class KmaruClient(Protocol):
	def send_a(self, payload):
		xml_dump = kmaru.lcia.xml_a(payload)
		self.transport.write(xml_dump)

	def send_r(self, payload):
		xml_dump = kmaru.lcia.xml_r(payload)
		self.transport.write(xml_dump)

	def connectionMade(self):
		print "Connection made with Server."
		login = kmaru.api.auth("0", "paultag", "hey")
		self.send_r(login)

	def dataReceived(self, data):
		print data

class KmaruClientFactory(ClientFactory):
	protocol = KmaruClient

	def clientConnectionFailed(self, connector, reason):
		print "Connection failed"
		reactor.stop()

	def clientConnectionLost(self, connector, reason):
		print "Connection lost"
		reactor.stop()

if __name__ == '__main__':
	factory = KmaruClientFactory()
	reactor.connectSSL('localhost', 2017, factory, ssl.ClientContextFactory())
	reactor.run()

