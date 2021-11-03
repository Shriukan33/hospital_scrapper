from pathlib import Path
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

BASE_DIR = Path(__file__).parent
FF_DRIVER_PATH = BASE_DIR / 'drivers' / 'geckodriver'

# Config of the browser
option = Options()
option.headless = True
service = Service(str(FF_DRIVER_PATH))
browser = webdriver.Firefox(service=service,
                            options=option)

# Retrieve credentials from JSON file
with open(BASE_DIR / 'credentials.json', 'r') as f:
    credentials = json.load(f)

# Store credentials in variables
login = credentials['id']
password = credentials['password']
login_url = credentials['login_url']

# Get to the login page
browser.get(login_url)

# Fill ID and password
login_field = browser.find_element(By.ID, 'ctl00_ctl00_ctl00_Contenu_TBLogin')
login_field.clear()
login_field.send_keys(login)

password_field = browser.find_element(By.ID,
                                      'ctl00_ctl00_ctl00_Contenu_TBPassword')
password_field.clear()
password_field.send_keys(password)

# Once filled, click on the login button
connect_button = browser.find_element(By.ID,
                                      'ctl00_ctl00_ctl00_Contenu_BValLogin')
connect_button.click()

browser.close()
