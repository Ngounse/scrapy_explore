import requests

# r = requests.get('https://xkcd.com/353/')

# print(r)
# print(dir(r))
# print(r.text)

## get request

payload = {'page': 2, 'count': 25}

r = requests.get('https://httpbin.org/get', params=payload)

# print(r.url)
##------------------

## post request

payload = {'username': 'ngounse', 'password': 'testing'}

r = requests.post('https://httpbin.org/post', data=payload)

# print(r.text)
# print(r.json())

r_dict = r.json()

# print(r_dict['form'])
##------------------

## get request basic-auth

r = requests.get('http://httpbin.org/basic-auth/ngounse/test', auth=('ngounse', 'test'))

print(r.text)

##------------------
