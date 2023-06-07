import datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
from db_connector import DBConnector

# Constants
host = 'sql.freedb.tech'
port = 3306
user = 'freedb_haggai'
password = '7p8Gc!Ycp!MB?%A'
database = 'freedb_users_10'
db = DBConnector(host, port, user, password, database)


user_id = 1
user_name = 'haggai'
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

driver = webdriver.Chrome(service=Service("C:\\chromedriver.exe"))
try:
    driver.get(f"http://127.0.0.1:5001/users/get_user_name/{user_id}")
    user_name_element = driver.find_element(by=By.ID, value="user_name")

    if user_name_element.text == user_name:
        print("Great news! We have found the ELEMENT", user_name_element.text)
    else:
        raise ValueError("User name does not match")

except NoSuchElementException:
    print("Element not found")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    driver.quit()
