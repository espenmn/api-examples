import json
import requests
import urllib
import urllib2


url = 'http://api.edipost.no/consignee'

API_KEY = '9953713dc7d97f7f7883b902e8205adf7ca1380e'


response = urllib2.urlopen(url).read()




params = urllib.urlencode({
  'api_key': API_KEY,
  'companyName': 'Doe Company'
  'name': 'Doe'
})
response = urllib2.urlopen(url, params).read()