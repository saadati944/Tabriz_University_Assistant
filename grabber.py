# imports
import requests
import config
import process

cookies = None


# get main web page
def get_mainpage():
    global cookies
    req = requests.get(config.mainpage, data=config.headers)
    cookies = req.cookies
    return req.content.decode('utf-8')


def login():
    global cookies
    req = requests.post(config.login_url, cookies=cookies, data=config.login_headers20)
    cookies = req.cookies
    return req.content.decode('utf-8')
