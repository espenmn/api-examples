import httplib2 as http
import json

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

def createConsignee():
	$body = file_get_contents('consignee.xml');

	API_KEY = '9953713dc7d97f7f7883b902e8205adf7ca1380e'

	#// Base URL to the REST service
	BASE_URL = 'http://api.edipost.no'
	path  =  '/consignee'


	headers = {
    	'Accept': 'application/json',
    	'Content-Type': 'application/json; charset=UTF-8'
	}

	target = urlparse(BASE_URL+path)
	method = 'GET'

	h = http.Http()

	h.add_credentials(auth.user, auth.password)

	response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)

	
	#return xml.attributes().id 
}



#return $data;
	
def postRequest( url, API_KEY, headers, body ):
	""" Do HTTP POST requests 
	""""	

	return data

	id = createConsignee()
print id"



# assume that content is a json reply
# parse content with the json module
data = json.loads(content)