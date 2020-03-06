#Password checker 

import requests 
import hashlib


#we should send the hash file usually, not the password itself (it is not secure), and we only provide the first five characters of the API

# response 400 - means something is wrong with the API

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/'+ query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
  return res 

def read_response(response):
  print(response.text)

def pwned_api_check(password):
  #check if password exists in API response from request_api_data
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5],sha1password[5:]
  # in the first variable we will store the first 5 characters, and in the second variable, we will store the remaining characters of the hash

  response = request_api_data(first5_char)
  return read_response(response)
  
  return sha1password

pwned_api_check('123')

