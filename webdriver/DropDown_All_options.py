import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_pythonVisibleTest:
    def test_pythoVisibleTest(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)  # based on need
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")
        driver.find_element(By.LINK_TEXT, 'Login').click()

        driver.find_element(By.NAME, 'username').send_keys('user1')
        driver.find_element(By.NAME, 'password').send_keys('Guru@12345')
        driver.find_element(By.NAME, 'password').submit()
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")

        # -------------------------------------------------------------
        # dropdown
        driver.find_element(By.ID, 'element10').click()
        driver.find_element(By.ID, 'element11').click()

        dropdown = driver.find_element(By.NAME, 'month')
        s=Select(dropdown)
        list_OF_options=s.options

        for i in list_OF_options:
            print(i.text)

        time.sleep(10)

r=Test_pythonVisibleTest()
r.test_pythoVisibleTest()