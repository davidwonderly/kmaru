#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

from twisted.internet import reactor, protocol, ssl
from twisted.internet.protocol import Factory, Protocol

import kmaru.api
import kmaru.lcia

import kmaru._protocol_callbacks

kmaru_callbacks = {
	"AUTH" : kmaru._protocol_callbacks.authProcessor
}

class KmaruServerMain(protocol.Protocol):
	def send_a(self, payload):
		xml_dump = kmaru.lcia.xml_a(payload)
		self.transport.write(xml_dump)

	def send_r(self, payload):
		xml_dump = kmaru.lcia.xml_r(payload)
		self.transport.write(xml_dump)

	def dataReceived(self, data):
		try:
			print "[log] incoming XML"
			incoming_payload = kmaru.lcia.readString(data)
			print "[log] good request."
			print "[log] class: " + incoming_payload['header']['class']

			try:
				kmaru_callbacks[incoming_payload['header']['class']](self, incoming_payload)
			except KeyError as e:
				print "[log] Oh shit. User fail. " + str(e)
				# err = kmaru.api.errora("-1", 1, "Failure to parse XML! Bad format!")
				# self.send_a(err)

		except KeyError as e:
			print "[log] Failure to parse incoming XML"
			err = kmaru.api.errora("-1", 1, "Failure to parse XML! Bad format!")
			self.send_a(err)

def run( port ):
    factory = protocol.ServerFactory()
    factory.protocol = KmaruServerMain
    reactor.listenTCP(port,factory)
    reactor.run()

def runssl( port, key, cert ):
	factory = Factory()
	factory.protocol = KmaruServerMain
	reactor.listenSSL(port, factory,
		ssl.DefaultOpenSSLContextFactory(
			key,
			cert
		)
	)
	reactor.run()
