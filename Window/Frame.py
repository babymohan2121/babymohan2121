import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Frame:
    def frame(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

        driver.switch_to.frame("packageListFrame")
        driver.find_element(By.XPATH,".//a[text()='org.openqa.selenium.chrome']").click()

        driver.switch_to.default_content()
        driver.switch_to.frame("packageFrame")
        driver.find_element(By.XPATH,".//a[text()='ChromeDriver']").click()

        driver.switch_to.default_content()
        driver.switch_to.frame("classFrame")
        driver.find_element(By.LINK_TEXT,'DEPRECATED').click()
        

        time.sleep(10)

a=Frame()
a.frame()