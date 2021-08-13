import time

from selenium import webdriver


class Test_Cookie:
    def test_cookie(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\chromedriver\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://apps.na.collabserv.com/sps/idp/saml11/login")

        cookie=driver.get_cookies()
        for i in cookie:
            print(i)


a=Test_Cookie()
a.test_cookie()
