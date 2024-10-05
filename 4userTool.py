import os
try:
    import requests
    import base64
    from uuid import uuid4
    import random
    from ms4 import InfoIG, RestInsta
    import requests
    import time
    import hashlib
    import uuid
    import json
    from secrets import token_hex
    from ms4 import Instagram
    import pycountry
    import random
    import mechanize
    from bs4 import BeautifulSoup
    from user_agent import generate_user_agent
except:
    os.system("pip install ms4 mechanize bs4 uuid requests faker user_agent pycountry")

import string
import json
from ms4 import UserAgentGenerator
import requests
import base64
from uuid import uuid4
import random
from ms4 import InfoIG, RestInsta
import requests
import time
import hashlib
import uuid
from secrets import token_hex
import pycountry
import random
import mechanize
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import threading
import requests
import random
import requests
import os
import uuid
from secrets import token_hex
import time
from user_agent import generate_user_agent
from ms4 import Instagram
from requests import get, post
from random import choice, randrange
import os, sys, uuid
import http.client
import requests
import re, uuid
import time
from time import sleep, time
from user_agent import generate_user_agent
from random import choice, randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import random
import os, requests, sys, time, datetime

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  
X = '\033[1;33m'  
Z1 = '\033[2;31m'  
F = '\033[2;32m'  
A = '\033[2;34m'  
C = '\033[2;35m'  
B = '\x1b[38;5;208m'  
Y = '\033[1;34m'  
M = '\x1b[1;37m'  
S = '\033[1;33m'
U = '\x1b[1;37m'  

print("\033[93m" + """ 
    ██╗  ██╗██╗   ██╗███████╗███████╗██████╗ 
    ██║  ██║██║   ██║██╔════╝██╔════╝██╔══██╗
    ███████║██║   ██║███████╗█████╗  ██████╔╝
    ╚════██║██║   ██║╚════██║██╔══╝  ██╔══██╗
         ██║╚██████╔╝███████║███████╗██║  ██║
         ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
          4user Letter Tool /by@d74.e                        
""")

print(f'''
{F}   [+] Telegram  : {X} d74ee|
{F}   [+] Instagram  : {X}d74.e |
{F}   [+] GitHub  : {X} Syd74e |
''')

token = input(f' {F} {C} Enter Token {C}:  ' + F)

ID = input(f' {F} {C} Enter ID{C} :  ' + F)


hit = 0
gg = 0
bb = 0
go = 0
bm = 0

def PLAY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
{C} Dev :  | D7 | User Tool
━━━━━━━━━━━━━━━━━━━━━━━━━
 {F} Done ✓  ~> 「{hit}」

 {B} Available IG  ~> 「{gg}」

 {Z}BAD IG  ~> 「{bb}」

 {Y}Good GM ~> 「{go}」

 {X}BAD X   ~> 「{bm}」

 {U} {U}email  ~> 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')

def tlg(email):
    global hit
    user = email.split("@")[0]
    hit += 1
    try:
        rest = RestInsta.Rest(user)["email"]
    except:
        rest = "Nothing To Rest"

    inf = InfoIG.Instagram_Info(user)
    name = inf["Name"]
    Id = inf["ID"]
    fols = inf["Followers"]
    folg = inf["Following"]
    bio = inf["Bio"]
    po = inf["Posts"]
    pr = inf["Is Private"]
    try:
        date = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()['date']
    except:
        date = None

    tlg = f'''

[+] Email ==> {email}
[+] Email Rest ==> {rest}
[+] Username ==> @{user}
[+] Name ==> {name}
[+] ID ==> {Id}
[+] Followers ==> {fols}
[+] Following ==> {folg}
[+] Bio ==> {bio}
[+] Date ==> {date}
[+] Posts ==> {po}
[+] Is Private ==> {pr}
[+] URL ==> https://www.instagram.com/{user}

𝐁𝐘 : @d74ee 
'''
    print(F + tlg)
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")

    with open('hits.txt', 'a') as f:
        f.write(tlg + '\n')

def get_username():
    global email
    while True:
        try:
            # تحديد الطول العشوائي (2، 3، أو 4 أحرف فقط)
            username_length = random.choice([4])
            
            # توليد اسم المستخدم بناءً على الطول المحدد
            username = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))
            
            # تكوين البريد الإلكتروني باستخدام اسم المستخدم
            email = username + "@gmail.com"
            
            # استدعاء الدالة Ahmed للتحقق من البريد الإلكتروني
            Ahmed(email)            
        except:
            pass

def Ahmed(email):
    global gg, bb
    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/"
    payload = "params=%7B%22client_input_params%22%3A%7B%22text_input_id%22%3A%22616z6k%3A71%22%2C%22was_headers_prefill_available%22%3A0%2C%22sfdid%22%3A%22%22%2C%22fetched_email_token_list%22%3A%7B%7D%2C%22search_query%22%3A%22"+email+"%22%2C%22android_build_type%22%3A%22release%22%2C%22accounts_list%22%3A%5B%5D%2C%22ig_android_qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22ig_oauth_token%22%3A%5B%5D%2C%22is_whatsapp_installed%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22was_headers_prefill_used%22%3A0%2C%22headers_infra_flow_id%22%3A%22%22%2C%22fetched_email_list%22%3A%5B%5D%2C%22sso_accounts_auth_data%22%3A%5B%5D%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22event_request_id%22%3A%22b8a5a2be-1abe-40da-b476-3d893c871e21%22%2C%22is_from_logged_out%22%3A0%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22waterfall_id%22%3A%22017145b8-cb79-439a-9036-2fb580f40ca0%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.6480220400074E13%2C%22is_platform_login%22%3A0%2C%22context_data%22%3A%22AR2rfU7knJNQCBz3hzsomH487qVyGu0HOVx3jgM-6G69fIwxA73vDmSlV7vY-W2aR4sv08iPPcsbdDt7RQF0ijGeqPudYXN0zlEZMvLeGOEvM_HHTtEJuv8dHDd4c8AIk4VpoaEASAIC9T_OS4yHwzupVtJKe7ghZ7k0y3kHeS7OGhaAIm4QvqfWW5JendkDb0mWJ31hcpuhEp8qcbdjJ27ABYmh7-MltY9OrlgAoBsSZuz8_MD3S1XQFV0I52liYk8fK_tSI9x4Ok0lTmIWJ4aN8pjQvxGhAWLJ73ONhBVfpIXE2xuutHN4eMrjKARC2-XcGRmg7pf3xLfGu_Z7zKiKrVmR8LQz91dwiKHFaND6DeHwVcARkBjYm0YLjaGdT-0FIeGYFs1x%7Carm%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb"
    headers = {
        'User-Agent': str(Agent.user()),
        'x-ig-app-locale': "en-US",
        'x-ig-device-locale': "en-US",
        'x-ig-mapped-locale': "en-US",
        'x-pigeon-session-id': "UFS-42175dfd-8675-4443-8f8d-7f09fa7ea9da-0",
        'x-pigeon-rawclienttime': "1725835735.847",
        'x-ig-bandwidth-speed-kbps': "-1.000",
        'x-ig-bandwidth-totalbytes-b': "0",
        'x-ig-bandwidth-totaltime-ms': "0",
        'x-bloks-version-id': "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
        'x-ig-www-claim': "0",
        'x-ig-device-id': "8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9",
        'x-ig-family-device-id': "2586e714-fdb4-4741-ba7b-0b84b13e2a97",
        'x-ig-android-id': "android-bf1b282ab2b0b445",
        'x-ig-timezone-offset': "10800",
        'x-fb-connection-type': "MOBILE.LTE",
        'x-ig-connection-type': "MOBILE(LTE)",
        'x-ig-capabilities': "3brTv10=",
        'x-ig-app-id': "567067343352427",
        'priority': "u=3",
        'accept-language': "en-US",
        'x-mid': "Zt4loQABAAFzGR1YLL2M9XOkL9El",
        'ig-intended-user-id': "0",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-fb-http-engine': "Liger",
        'x-fb-client-ip': "True",
        'x-fb-server-cluster': "True"
    }
    try:
        req = requests.post(url, data=payload, headers=headers).text
        
        if '"status":"ok"' in req:
            if "The password you entered is incorrect." in req or "We sent a code to your email. Enter that code to confirm your account." in req:
                gg += 1
                PLAY()
                check_gmail(email)
            elif "Please wait a few minutes before you try again." in req:
                Ch(email)
            else:
                bb += 1
                PLAY()
        else:
            Ch(email)
    except:
        Ch(email)

# توليد وكيل المستخدم
class Agent:
    @staticmethod
    def user():
        ii = ["165.1.0.29.119", "166.0.0.30.120", "167.0.0.31.121", "168.0.0.32.122"]
        aa = {
            "28/9": ["720dpi", "1080dpi", "1440dpi"],
            "29/10": ["720dpi", "1080dpi", "1440dpi", "2160dpi"],
            "30/11": ["1080dpi", "1440dpi", "2160dpi"],
            "31/12": ["1440dpi", "2160dpi"]
        }
        ss = {
            "720dpi": ["1280x720", "1920x1080"],
            "1080dpi": ["1920x1080", "2560x1440", "3840x2160"],
            "1440dpi": ["2560x1440", "3840x2160"],
            "2160dpi": ["3840x2160", "7680x4320"]
        }
        dd = {
            "samsung": ["SM-T292", "SM-G973F", "SM-A515F"],
            "google": ["Pixel 4", "Pixel 5"],
            "huawei": ["P30 Pro", "Mate 40 Pro"],
            "xiaomi": ["Mi 10", "Redmi Note 10"],
            "oneplus": ["8T", "9 Pro"],
            "sony": ["XZ2", "Xperia 1"]
        }
        cc = ["qcom", "exynos", "kirin", "mediatek", "apple"]
        lan = ["en_US", "es_ES", "fr_FR", "de_DE", "zh_CN", "ja_JP", "ko_KR"]
        dp = ["phone", "tablet", "watch", "tv", "car"]
        arm = ["arm64_v8a", "armeabi-v7a", "x86", "x86_64"]
        comb = ["samsung", "google", "huawei", "xiaomi", "oneplus", "sony"]

        sos = random.choice(list(aa.keys()))
        vlo = random.choice(aa[sos])
        lop = random.choice(ss[vlo])
        ki = random.choice(comb)
        mo = random.choice(dd.get(ki, ["Unknown"]))

        user_agent = (
            f"Instagram {random.choice(ii)} Android "
            f"({sos}; {vlo}; {lop}; {ki}; {mo}; "
            f"{random.choice(arm)}; {random.choice(dp)}; "
            f"{random.choice(lan)}; {random.choice(cc)})"
        )

        return user_agent

# تهيئة المتغيرات
class Variable:
    country = [country.numeric for country in pycountry.countries]
    num = random.choice(country)
    sgin = hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
    csr = str(token_hex(8) * 2)
    android = f"android-{uuid.uuid4().hex[:16]}"

# بدء التنفيذ
threads = []
for i in range(10):
    t = threading.Thread(target=get_username)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
    