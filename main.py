# -*- coding: utf-8 -*-

import os
import re
import sys
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_BASE = 'https://www.instagram.com'
HEADLESS_MODE = True

if len(sys.argv) is not 2:
    logging.error('対象のユーザーIDをコマンドライン引数に渡してください')
    sys.exit()

chrome_options = Options()
if HEADLESS_MODE:
    chrome_options.add_argument("--headless")

executable_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'chromedriver'
    )

driver = webdriver.Chrome(
        executable_path=executable_path,
        options=chrome_options
    )

user_id = sys.argv[1]
url = URL_BASE + '/' + user_id 
driver.get(url)
locator = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
follower = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located(locator))

follower_count = re.sub("\\D", "", follower.text)
print(follower_count)
driver.quit()