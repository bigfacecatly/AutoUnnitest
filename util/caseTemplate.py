


import os
import requests
import unittest
# from util.screen_shot import screenshot_config
# from util.ace_login import login
file_path = os.path.dirname(os.path.dirname(__file__))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Template(unittest.TestCase):
    def setUp(self):
        self.headers = self.login()
        self.driver = self.screenshot_config()
    def tearDown(self):
        self.driver.quit()

    #接口登陆ace平台
    def login(self):
        url = ''
        data = {

        }

        r = requests.post(url=url, data=data)
        uid, token = r.json()['data']['uid'], r.json()['data']['token']
        headers = {

        }
        return headers

    #截图
    def screenshot_config(self,url=""):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chrome_options,
                                  executable_path=file_path + "/chromedriver")
        driver.get(url)
        login_name = driver.find_element_by_id('login_username')
        time.sleep(0.5)
        login_name.send_keys('test')
        login_passwd = driver.find_element_by_id('login_password')
        login_passwd.send_keys('test')
        time.sleep(0.5)
        submit = driver.find_element_by_tag_name('button')
        submit.click()
        # print('driver111111',driver)
        return driver

