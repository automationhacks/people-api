import requests

wrong_payload = {
    'username': 'raiyeem',
    'password': '1245'
}

right_payload = {
    'username': 'Raiyeem',
    'password': '1245'
}

wrong_r = requests.post('https://httpbin.org/basic-auth', data=wrong_payload)

print(wrong_r.status_code)

#print(wrong_dict)