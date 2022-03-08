from pprint import PrettyPrinter, pprint
import requests

payload = {
    'username': 'raiyeem',
    'pass': '12345'
}

r = requests.post('https://httpbin.org/post', data= payload)

print(r.text) # will print the whole request

r_dict = r.json()

print('******************************')
pprint(r_dict['form']) # accessing the form value of that json 