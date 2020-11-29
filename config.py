# This file contains the program settings

import json

data=dict()
with open('./data.json', 'r') as f:
    data=json.loads(f.read())


# main page of the site
mainpage = data["mainpage"]

# http header to say the server that we are a browser in windows 10 so the server will not refuse the connection
headers data["headers"]

# headers={}
login_url = data["login_url"]

login_headers20 = data["login_headers20"]