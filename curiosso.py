
# import libraries
import hashlib
import time

# user inputs their target URL
targurl = raw_input("What is your target url?")

# user inputs their organization sso ID
ssoid = raw_input("What is your organization sso ID?")

# user inputs their secret key
key = raw_input("What is your secret key?")

# record today's date (yyyymmdd)
date = time.strftime('%Y%m%d')

# create sso url
ssourl = "/sso/" + ssoid + targurl[16:]

# combine string to be hashed
hashed = key + ssourl + date

# get token
token = hashlib.md5(hashed).hexdigest()

# print token
print("\n\nToken: " + token)

# print authenticated url
print("\n\nAuthenticated URL: " + "https://curio.ca" + ssourl + "?token=" + token + "\n\n")
