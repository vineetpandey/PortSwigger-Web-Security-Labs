import requests
from bs4 import BeautifulSoup

# For deprecating the warnings
requests.packages.urllib3.disable_warnings()

# Initializing Session object
s = requests.Session()

# Determine proxy details to intercept the request within the burp proxy
s.proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

user = 'test1'
pwd = 'test2'

r_get = s.get("https://abc.com:123/cas/login", verify=False)
print r_get.headers, '\n'

# Using beautifulsoup library to extract the desired data/parameter values from the downloaded page to initiate the necessary actions
data = []
soup = BeautifulSoup(r_get.text, features="lxml")
data = data + soup.find_all("div", {"class" : "login btn-login"})

for i in data:
	lt = i.find_all("input")[0]["value"]
	execution = i.find_all("input")[1]["value"]
	
# print lt
# print execution

_eventId = "submit"
submit = "Login"

data = {"username":user, "password":pwd, "lt":lt, "execution":execution, '_eventId':_eventId, 'submit':submit}
r = s.post("https://abc.com:123/cas/login?service=https://abc.com:456/app/cas_security_check", verify=False, data=data, allow_redirect=True)

print "\nAfter login headers: \n", r.headers

r_postlogin = s.get("https://abc.com:456/app/application1.html", verify=False, allow_redirect=True)

print "\n---------------------------------------"
print "\nRequest Headers that were sent to server: \n", r_postlogin.request.headers
print "\n---------------------------------------"
print "Response Headers after resource request: \n", r_postlogin.headers
print "Response Status Code: ",r_postlogin.status_code, "\n"
