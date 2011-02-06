#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

from twisted.internet import ssl, reactor
from twisted.internet.protocol import ClientFactory, Protocol

import twisted.internet.error

import kmaru.api
import kmaru.lcia

import kmaru._client_protocol_callbacks

kmaru_callbacks = {
	"AUTHA" : kmaru._client_protocol_callbacks.authAnswerProcessor
}

class KmaruClient(Protocol):
	def send_a(self, payload):
		xml_dump = kmaru.lcia.xml_a(payload)
		self.transport.write(xml_dump)

	def send_r(self, payload):
		xml_dump = kmaru.lcia.xml_r(payload)
		self.transport.write(xml_dump)

	def connectionMade(self):
		if self.username != None and self.password != None:
			login = kmaru.api.auth(
				"0",
				self.username,
				self.password
			)
			self.send_r(login)
		else:
			KeyError("No Username and such")

	def dataReceived(self, data):
		try:
			incoming_payload = kmaru.lcia.readString(data)
			kmaru_callbacks[incoming_payload['header']['class']](self, incoming_payload)

		except KeyError as e:
			print "[log] Failure to parse incoming XML"
			err = kmaru.api.errora("-1", 1, "Failure to parse XML! Bad format!")
			self.send_a(err)

class KmaruClientFactory(ClientFactory):
	protocol = KmaruClient

	def setAuth( self, username, password ):
		self.protocol.username = username
		self.protocol.password = password

	def stop(self):
		try:
			reactor.stop()
		except twisted.internet.error.ReactorNotRunning as e:
			pass

	def clientConnectionFailed(self, connector, reason):
		print "Connection failed"
		self.stop()

	def clientConnectionLost(self, connector, reason):
		print "Connection lost"
		self.stop()

def runssl(port, host, username, password):
	factory = KmaruClientFactory()
	factory.setAuth(username, password)
	reactor.connectSSL(
		host,
		port,
		factory,
		ssl.ClientContextFactory()
	)
	reactor.run()
