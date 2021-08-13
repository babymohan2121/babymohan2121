import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Double:
    def double(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")
        driver.find_element(By.LINK_TEXT, 'Login').click()

        driver.find_element(By.NAME, 'username').send_keys('mohanasundaram')
        driver.find_element(By.NAME, 'password').send_keys('mohan2121')
        driver.find_element(By.NAME, 'password').submit()
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")

        driver.find_element(By.ID, 'element20').click()
        driver.find_element(By.ID, 'element24').click()

        dbclick=driver.find_element(By.ID,'dbclick1')
        a=ActionChains(driver)
        a.double_click(dbclick).perform()
        time.sleep(10)

a=Double()
a.double()