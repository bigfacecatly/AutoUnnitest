

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,sys,os

def demo1():
    print("hello world")

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.dirname(os.path.dirname(__file__))
#截图功能
# def screenshot_config(url,headers="lang=zh_CN.UTF-8"):
def screenshot_config(url="https://ace-test.altstory.com/login"):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options,
                              executable_path=file_path+"/chromedriver")
    driver.get(url)
    login_name = driver.find_element_by_id('login_username')
    login_name.send_keys('test')
    login_passwd = driver.find_element_by_id('login_password')
    login_passwd.send_keys('test')
    submit = driver.find_element_by_tag_name('button')
    submit.click()
    time.sleep(1)
    return driver
def screenshot(url,p_name,driver):
    driver.get(url)
    # time.sleep(2)
    # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    # print(width, height)
    # 设置宽跟高
    driver.set_window_size(width, height)
    try:
        time.sleep(0.5)
        picture_url = driver.get_screenshot_as_file('report/screen/'+p_name+".png")
    except BaseException as msg:
        print(msg)


if __name__ == '__main__':
    url="https://ace-test.altstory.com/login"
    screenshot_config(url)