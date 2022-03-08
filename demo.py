from pprint import PrettyPrinter, pprint
import requests
# r is set as variable
# It's value is set by using requests library and with a get request 
r = requests.get('https://xkcd.com/353/')
pprint(r.text)

print(r.status_code) # prints the response code

print(r.ok) # this one just give you if the request was successful and it gives out True or False 


