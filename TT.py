import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Table:
    def table(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.w3schools.com/html/html_tables.asp")

        table=driver.find_element(By.XPATH,".//table[@id='customers']")
        row=table.find_elements(By.TAG_NAME,'tr')


        for i in row:
            column=i.find_elements(By.TAG_NAME,'td')
            for j in column:
                print(j.text,end="  ")
            print()
        time.sleep(10)


a=Table()
a.table()