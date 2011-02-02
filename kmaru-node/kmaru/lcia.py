#
# GPL and shit
#

from xml.dom.minidom import Document

root_node = "lcia"

def xml_r( r_payload ):
	try:
		doc = Document()
		lcia = doc.createElement("lcia")
		doc.appendChild(lcia)

		headers = doc.createElement("headers")
		lcia.appendChild(headers)

		klass = doc.createElement("class")
		sid   = doc.createElement("sid")

		headers.appendChild(klass)
		headers.appendChild(sid)

		class_text = doc.createTextNode(r_payload['class'])
		sid_text   = doc.createTextNode(str(r_payload['sid']))

		klass.appendChild(class_text)
		sid.appendChild(sid_text)

		# OK. Headers locked and loaded.

		data = doc.createElement("data")
		lcia.appendChild(data)

		for x in r_payload['data']:
			node = doc.createElement(x)
			info = doc.createTextNode(r_payload['data'][x])
			node.appendChild(info)
			data.appendChild(node)

		xml_string = doc.toprettyxml(indent="  ")
		return xml_string;
	except KeyError:
		print "Oh holyshit"
	
