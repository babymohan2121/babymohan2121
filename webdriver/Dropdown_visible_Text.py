import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dropdown:
    def dropdown(self):

            driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
            driver.maximize_window()
            driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
            drop=driver.find_element(By.ID,'RESULT_RadioButton-9')

            s=Select(drop)
            s.select_by_visible_text('Evening')
            time.sleep(10)


a=Dropdown()
a.dropdown()