from dataclasses import replace
import requests
import platform
import os
xox = platform.platform()[::-1].replace('.','').replace(' ','').replace('-','').upper()
svr = requests.get('https://raw.githubusercontent.com/sameerpanhwarit/test/server.txt').text

print('This is Your token: ',xox)

print('-'*50)

if xox in svr:
    print("Your Subscription On.")

else:
    print("Please Buy This Tool")
