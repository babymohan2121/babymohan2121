import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_DisableInfoBarTest:
    def test_disableInfoBarTest(self):
        options =webdriver.ChromeOptions()
        options.headless = True

        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe",chrome_options=options)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        data=driver.title
        print(data)

        time.sleep(10)

r=Test_DisableInfoBarTest()
r.test_disableInfoBarTest()