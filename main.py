#Make sure that this code is above your current one.

#Imports
import subprocess, requests, time, os

#Strings
hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
site = requests.get('TYPE SITE HERE')


#Actual Authentication System
try:
    if hardwareid in site.text:
        pass
    else:
        print('[ERROR] HWID NOT in database')
        print('[HWID:' + hardwareid + ']') 
        time.sleep(5)
        os._exit()
except:
    print('[ERROR] FAILED to connect to database')
    time.sleep(5) 
    os._exit() 
    
#Your actual project comes under here:
print('Success.')
input()
