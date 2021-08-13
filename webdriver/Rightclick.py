import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Rightclick:
    def rightclick(self):
            driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
            driver.maximize_window()
            driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
            right=driver.find_element(By.XPATH,".//span[text()='right click me']")
            a=ActionChains(driver)
            a.context_click(on_element=right).perform()

            a.send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(10)

x=Rightclick()
x.rightclick()