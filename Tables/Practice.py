import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_StaticTableTest:
    def test_staticTableTest(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)  # based on need
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")
        driver.find_element(By.LINK_TEXT, 'Login').click()

        driver.find_element(By.NAME, 'username').send_keys('user1')
        driver.find_element(By.NAME, 'password').send_keys('Guru@12345')
        driver.find_element(By.NAME, 'password').submit()
        driver.get("http://djangovinoth.pythonanywhere.com/labhome/")

        # -------------------------------------------------------------
        # dropdown
        driver.find_element(By.ID, 'element39').click()
        driver.find_element(By.ID, 'element40').click()

        print("S.NO",    "NAME",    "MOBILE",    "E-MAIL",    "PLACE"  )

        table=driver.find_element(By.XPATH,".//table[@id='table1']")
        row=len(table.find_elements(By.XPATH,'//*[@id="table1"]/tbody/tr'))
        col=len(table.find_elements(By.XPATH,'//*[@id="table1"]/thead/tr/th'))

        print(row)
        print(col)

        for r in range(1,row+1):
            for c in range(1,col+1):
                    data=driver.find_element(By.XPATH,"//*[@id='table1']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
                    print(data.text,end='  ')
            print()

        time.sleep(5)


r=Test_StaticTableTest()
r.test_staticTableTest()
