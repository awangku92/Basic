import requests

r = requests.get('http://localhost:5001/')
#r = requests.post('http://localhost:5001/t')
#r = requests.put('http://localhost:5001/t')

print (r._content)