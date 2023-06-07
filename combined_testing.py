import json
import pymysql
import datetime

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Constants
schema_name = "freedb_users_10"
db_host = 'sql.freedb.tech'
db_port = 3306
db_user = 'freedb_haggai'
db_pass = '7p8Gc!Ycp!MB?%A'
db_name = 'freedb_users_10'
conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_name)


user_id = int(input("enter user id"))
user_name = input("enter user name")
url = f"http://127.0.0.1:5000/data/{user_id}"

# payload data

data = {'user_id': f'{user_id}',
        'user_name': f'{user_name}',
        'creation_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
# create a new user

try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    print("Post request successful, new user added", "-", user_name)
except requests.exceptions.RequestException as err:
    print("except_post request failed:", err)

# check if the user and id that i entered before, is in db.

try:
    get_res = requests.get(url)
    if get_res.json()[0] == user_id and get_res.json()[1] == user_name:
        print("The user and ID you entered is in the same row in database")
    else:
        raise get_res
except:

    print("Except_testing ERROR")

# search element that contains the user_name.

driver = webdriver.Chrome(service=Service("C:\\chromedriver_win32\\chromedriver.exe"))
try:
    driver.get(f"http://127.0.0.1:5001/users/get_user_name/{user_id}")
    user_name_element = driver.find_element(by=By.ID, value="user_name")

    if user_name_element.text == user_name:
        print("Great news! We have found the ELEMENT", user_name_element.text)
    else:
        raise user_name_element.text
except:
    print("except_element NOT found")

pass
print("code end")
