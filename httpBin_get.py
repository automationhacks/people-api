import requests

payload = {'page': 2, 'count': 25}  # instead of adding params in the get request this helps to build a clear way to send request.
r = requests.get('https://httpbin.org/get', params=payload) # the payload is sent as parameter
print(r.text) # shows the api request (Total)

print(r.url) # prints the full endpoint