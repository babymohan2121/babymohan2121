import time

from selenium import webdriver


class Screen:
    def screen(self):

        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com/")
        driver.save_screenshot("\\Users\\mohan\\PycharmProjects\\selenium_webdriver\\Window\\picture.png")
        time.sleep(5)


a=Screen()
a.screen()
