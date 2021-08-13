from selenium import webdriver
from selenium.webdriver.common.by import By


class Table:
    def table(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.w3schools.com/html/html_tables.asp")

        table=driver.find_elements(By.XPATH,".//table[@id='customers']//td")

        for i in table:
            print(i.text)
            if i.text=='Germany':
                print("Germany is present")





a=Table()
a.table()