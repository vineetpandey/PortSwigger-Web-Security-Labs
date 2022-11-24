# Lab: Reflected XSS into HTML context with nothing encoded

import requests
# from bs4 import BeautifulSoup

# For deprecating the warnings
requests.packages.urllib3.disable_warnings()

# Initializing Session object
s = requests.Session()

# Determine proxy details to intercept the request within the burp proxy
# s.proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

r = requests.get("https://api.github.com/events")

headers = r.headers

f = open('headers.txt', 'w+')

f.write('\n----------------------------------------------------')
f.write('\n\n\t\t\t\t\t Headers Info')
f.write('\n\n----------------------------------------------------\n')
f.write('\nContent-Security-Policy: '+ headers['Content-Security-Policy'])
f.write('\nAccess-Control-Allow-Origin: '+ headers['Access-Control-Allow-Origin'])
f.write('\nCache-Control: '+ headers['Cache-Control'])
f.write('\nContent-Type: '+headers['Content-Type'])
f.write('\nContent-Encoding: '+headers['Content-Encoding'])
f.write('\nETag: '+ headers['ETag'])
#f.write('\nLink: '+ headers['Link'])
f.write('\nReferrer-Policy: '+ headers['Referrer-Policy'])
f.write('\nServer: '+ headers['Server'])
# f.write('\nStatus: '+ headers['Status'])
f.write('\nStrict-Transport-Security: '+ headers['Strict-Transport-Security'])
f.write('\nX-Content-Type-Options: '+ headers['X-Content-Type-Options'])
f.write('\nX-Frame-Options: '+ headers['X-Frame-Options'])
f.write('\nX-XSS-Protection: '+ headers['X-XSS-Protection'])
f.write('\n\n----------------------------------------------------\n')
f.write('\n\n\t\t\t\t\t Raw Header Details')
f.write('\n\n----------------------------------------------------\n')
s=str(headers)
f.write(s)
f.write('\n\n////////////////////////////////////////////////////\n')
f.write('\n# Below are few resources basis mentioned headers...')
f.write('\n------------------------------------------------------')
f.write('\n******************************************************')
f.write('\n# Referrer-Policy is a security header designed to prevent cross-domain Referer leakage. \n*Link - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy')
f.write('\n---------------------------------------------')
f.write('\n# Content Security Policy - \n*Link - https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP')
f.write('\n---------------------------------------------')
f.write('\n# Access-Control-Expose-Headers - \n*Link - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers')
f.write('\n---------------------------------------------')
f.write('\n# Access-Control-Allow-Origin - \n*Link - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin')
f.write('\n---------------------------------------------')
f.write('\n# Strict-Transport-Security - \n*Link - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security')
f.write('\n---------------------------------------------')
f.write('\n# X-Content-Type-Options - \n*Link - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options')
f.write('\n---------------------------------------------')
f.write('\n# X-Frame-Options - \n*Link - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options')
f.write('\n---------------------------------------------')
f.write('\n# X-XSS-Protection - \n*Link - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection')
f.write('\n---------------------------------------------')
f.close()