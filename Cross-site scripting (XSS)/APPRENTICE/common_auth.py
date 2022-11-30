import requests
import sys
# For deprecating the warnings
requests.packages.urllib3.disable_warnings()

# Determine proxy details to intercept the request within the burp proxy
# s.proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        username = sys.argv[2].strip()
        password = sys.argv[3].strip()
    except Exception:
        print("[-] Usage: %s <url> <username> <password>" % sys.argv[0])
        print('[-] Example: %s www.example.com user1 mypass' % sys.argv[0])
        sys.exit(-1)
