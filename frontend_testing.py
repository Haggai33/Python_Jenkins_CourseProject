import time
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

get_user = 1

driver = webdriver.Chrome(service=Service("C:\\chromedriver_win32\\chromedriver.exe"))

driver.get(f"http://127.0.0.1:5001/users/get_user_name/{get_user}")

try:
    user_name_element = driver.find_element(by=By.ID, value="user_name")
    print("Great news! We have found the user you were looking for. - ", user_name_element.text)
    driver.implicitly_wait(10)

except:
    print("We're sorry, but we couldn't find the user you searched for")



