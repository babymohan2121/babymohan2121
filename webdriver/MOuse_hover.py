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
        driver.find_element(By.ID, 'element27').click()

        mouse=driver.find_element(By.XPATH,".//a[text()='Resume']")

        item=driver.find_element(By.ID,'id13')

        Havoc=driver.find_element(By.ID,'id17')

        a=ActionChains(driver)
        a.move_to_element(mouse).perform()
        time.sleep(5)
        a.move_to_element(item).perform()
        time.sleep(5)
        a.move_to_element(Havoc).perform()
        a.click(Havoc).click()
        time.sleep(10)

a=Double()
a.double()