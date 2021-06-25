#I hardly recommend using login system, because hwid is not as safe as it and can get cracked easily.

import subprocess, requests, time, os

hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
#Type any site that contains easily accesable text.
site = requests.get('TYPE SITE HERE')
#The only examples i can think of are raw pastebin and raw github text


try:
    if hardwareid in site.text:
        pass
    else:
        print('[ERROR] HWID Not in database')
        print('[HWID:' + hardwareid + ']') 
        time.sleep(5)
        os._exit()
except:
    print('[ERROR] Failed to connect to database')
    time.sleep(5) 
    os._exit() 
    

print('Success.')
input()