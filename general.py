# Functions for general use
from os.path import basename, splitext
from urllib.parse import urlparse, urlunparse, ParseResult

# Verify if a path is a file path and not a html page 
def isFilePath(fullpath):
	base = basename(fullpath)
	name, ext = splitext(base)
	return ((ext != '') & ('htm' not in ext) & ('php' not in ext) & (ext not in ['.asp', '.aspx', '.xml', '.phl', '.jsp']))

assert(isFilePath('/path/some/thing') == False)
assert(isFilePath('/path/some/thing/new.thing'))
assert(isFilePath('/path/some/thing/new.html') == False)

# Verify if a link addresses a file
def hasFileAtLink(link):
	return isFilePath(urlparse(link).path)

assert(isFilePath('www.lba.bla.com/path/some/thing/new.thing?dfasdfk'))
assert(isFilePath('www.adlf.adk.us/path/some/thing') == False)

# initial location is where you start the scraping
def extractLocationPath(link, initialLocation=''):
	location = urlparse(initialLocation)
	result = urlparse(link)
	if (result.netloc == ''):
		return urlunparse(ParseResult(location.scheme, location.netloc,(result.path if result.path != '/' else ''),'','',''))
	else:
		return urlunparse(ParseResult(result.scheme, result.netloc,(result.path if result.path != '/' else ''),'','',''))

# Is link of the same location of the page of the scraping

def isSubPageOfLocation(link, initialLocation):
	location = urlparse(initialLocation)
	result = urlparse(link)
	return ((result.netloc == '') | (location.netloc == result.netloc))

