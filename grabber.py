# imports
import requests
import config

cookies = None


# get main web page
def get_mainpage():
    global cookies
    req = requests.get(config.mainpage, data=config.headers)
    cookies = req.cookies
    return req.content.decode('utf-8')
