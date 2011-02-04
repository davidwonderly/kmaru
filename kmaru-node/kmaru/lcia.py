#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

import xml.dom.minidom
from xml.dom.minidom import Document

required_r_headers = [
	"class",
	"sid",
	"time",
]

required_a_headers = [
	"class",
	"sid",
	"time",
	"errors",
	"msg",
]

def readString(data):
	try:
		data = xml.dom.minidom.parseString(data)
		payload = interp_xml(data)
		return payload
	except xml.parsers.expat.ExpatError as e:
		KeyError("Failure to parse XML")

def interp_xml(data):

	heads = data.getElementsByTagName("headers").item(0).childNodes[0]
	headers = {}
	while heads.nextSibling != None:
		heads = heads.nextSibling
		if heads.nodeType == heads.ELEMENT_NODE: #Fucking fix me, bittttttch.
			headers[heads.nodeName] = heads.childNodes[0].data.strip()


	datas = data.getElementsByTagName("data").item(0).childNodes[0]
	datas = {}
	while heads.nextSibling != None:
		heads = heads.nextSibling
		if heads.nodeType == heads.ELEMENT_NODE: #Fucking fix me, bittttttch.
			headers[heads.nodeName] = heads.childNodes[0].data.strip()


	ret = {}
	ret['header'] = headers
	ret['data']   = datas

	return ret

def xml_r(payload):
	return _xml_parse( required_r_headers, payload )

def xml_a(payload):
	return _xml_parse( required_a_headers, payload )

def _xml_parse( required_headers, payload ):
	try:
		doc = Document()
		lcia = doc.createElement("lcia")
		doc.appendChild(lcia)

		headers = doc.createElement("headers")
		lcia.appendChild(headers)

		for x in required_headers:
			node = doc.createElement(x)
			info = doc.createTextNode(str(payload['header'][x]))
			node.appendChild(info)
			headers.appendChild(node)

		data = doc.createElement("data")
		lcia.appendChild(data)

		for x in payload['data']:
			node = doc.createElement(x)
			info = doc.createTextNode(payload['data'][x])
			node.appendChild(info)
			data.appendChild(node)

		xml_string = doc.toprettyxml(indent="  ")
		return xml_string;
	except KeyError:
		raise KeyError("Missing Header")

