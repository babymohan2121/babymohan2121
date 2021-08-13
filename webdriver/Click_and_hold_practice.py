import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Click_Hold:
    def click_hold(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://selenium08.blogspot.com/2020/01/click-and-hold.html")

        x=driver.find_element(By.XPATH,".//li[text()='C']")

        driver.execute_script('arguments[0].scrollIntoView();',x)

        a=ActionChains(driver)
        a.click_and_hold(on_element=x).perform()

        time.sleep(5)

a=Click_Hold()
a.click_hold()
