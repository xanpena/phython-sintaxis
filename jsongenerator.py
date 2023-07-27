import json 

print dir(json)
#['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'json']
#['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'json']

url = 'https://next.json-generator.com/api/json/get/VkPaJA1TH'
from urllib2 import urlopen
r = urlopen(url)
#r.read()
data = json.loads(r.read())
#print data
#print data[1]
print data[1]['_id']
print data[1]['name']

st = json.dumps(data)
print st