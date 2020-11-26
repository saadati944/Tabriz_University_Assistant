import grabber
import config

# print(grabber.get_mainpage())
config.login_headers["ctl00$mainContent$UserName"] = input('enter username : ')
config.login_headers["ctl00$mainContent$Password"] = config.login_headers["ctl00$mainContent$hdfPass"] = input(
    'enter password : ')

with open('file1.html', 'w', encoding='utf-8') as f:
    f.write(grabber.get_mainpage())

input('first page loaded successfully !!!\npress enter to continue...')

print()


with open('file2.html', 'w', encoding='utf-8') as f:
    f.write(grabber.login())


input('second page loaded successfully !!!\n\n!!!   check file1.html & file2.html   !!!\n\npress enter to continue...')
