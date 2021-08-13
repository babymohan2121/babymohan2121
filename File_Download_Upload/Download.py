import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test_Upload:
    def test_upload(self):
        options =webdriver.ChromeOptions()
        options.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\\mohan\\Documents"})

        driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe",chrome_options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)  # based on need
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")
        driver.find_element(By.LINK_TEXT, 'Login').click()

        driver.find_element(By.NAME, 'username').send_keys('user1')
        driver.find_element(By.NAME, 'password').send_keys('Guru@12345')
        driver.find_element(By.NAME, 'password').submit()
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")

        driver.find_element(By.ID, 'element1').click()
        driver.find_element(By.ID, 'element8').click()

        driver.find_element(By.XPATH,".//a[@id='download']").click()

        time.sleep(10)

r=Test_Upload()
r.test_upload()