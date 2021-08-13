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

        print("------------------------------------------------------------------")
        mycookie={'name':'MY mohan Cookie','value':'12345'}
        driver.add_cookie(mycookie)

        j=driver.get_cookies()
        for k in j:
            print(k)

        print("----------------------------------------------------------------------")
        print("delete the newly added cookie")
        driver.delete_cookie('MY mohan Cookie')
        m=driver.get_cookies()
        print(m)

        print("cookies are deleted")

a=Test_Cookie()
a.test_cookie()
