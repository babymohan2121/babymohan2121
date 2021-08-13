import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_SimpleAlertTest:
    def test_simpleAlertTest(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)  # based on need
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")
        driver.find_element(By.LINK_TEXT, 'Login').click()

        driver.find_element(By.NAME, 'username').send_keys('user1')
        driver.find_element(By.NAME, 'password').send_keys('Guru@12345')
        driver.find_element(By.NAME, 'password').submit()
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")

        driver.find_element(By.ID, 'element1').click()
        driver.find_element(By.ID, 'element7').click()

        click_me=driver.find_element(By.XPATH,".//input[@id='id2']")
        click_me.click()

        a=driver.switch_to.alert
        data=a.text
        print(data)

        a.dismiss()

        time.sleep(10)

r=Test_SimpleAlertTest()
r.test_simpleAlertTest()