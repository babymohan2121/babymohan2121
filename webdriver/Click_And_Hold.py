import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Click_Hold:
    def click_hold(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.geeksforgeeks.org/")

        hold=driver.find_element(By.XPATH,".//a[text()='Courses']")
        a=ActionChains(driver)
        a.click_and_hold(on_element=hold).perform()
        time.sleep(5)
        driver.find_element(By.XPATH,".//span[text()='Tutorials']").click()
        time.sleep(5)

a=Click_Hold()
a.click_hold()
