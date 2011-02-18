modules  = {}
mod_info = {}

def addModule( name, fn ):
	modules[name] = fn
	
def runMod( name, args ):
	modules[name](args);

def addModDescr( name, descr ):
	mod_info[name] = descr

def getModDescr( name ):
	try:
		return mod_info[name]
	except KeyError:
		return ""
