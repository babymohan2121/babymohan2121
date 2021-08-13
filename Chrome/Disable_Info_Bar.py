import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_DisableInfoBarTest:
    def test_disableInfoBarTest(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe",chrome_options=options)
        driver.maximize_window()
        driver.get("https://www.google.com/")

        time.sleep(10)

r=Test_DisableInfoBarTest()
r.test_disableInfoBarTest()