from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

BASE_DIR = Path(__file__).parent
FF_DRIVER_PATH = BASE_DIR / 'drivers' / 'geckodriver'

option = Options()
option.headless = True
service = Service(str(FF_DRIVER_PATH))

browser = webdriver.Firefox(service=service,
                            options=option)
browser.get('https://google.com/')
print(browser.title)
browser.close()
