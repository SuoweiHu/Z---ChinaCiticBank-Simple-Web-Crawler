# This program will login ISIS platform of ANU website 
# and craw grade related info for the login student

import requests 
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Site's URL
# url = "https://segmentfault.com/a/1190000003933903"
url = "https://idp2.anu.edu.au/idp/profile/SAML2/Redirect/SSO?execution=e1s1"

# Request header 
head_UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
head_referer = "https://www.anu.edu.au/"
head = {
    "User-Agent" : head_UserAgent,
    "Referer" : head_referer
}

# Request data 
data = {
    "j_username" : "u6966459",          # Account 
    "j_password" : "XXXXXXXX",          # Password 
    "donotcache" : "1",                 # Dont remember login
    "_shib_idp_revokeConsent" : "true"  # Clear prior logins
    "_eventId_proceed":""
}

# Make request and get result website
response = requests.post(url, data=data)
print(response.text)