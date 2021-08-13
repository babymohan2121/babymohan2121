import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_MultiWindowTest:
    def test_multiWindowTest(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)  # based on need
        driver.get("http://book.theautomatedtester.co.uk/chapter1")
        driver.find_element(By.XPATH,".//div[text()='Click this link to launch another window']").click()

        #find sessions using window handles
        session=driver.window_handles

        for totalsession in session:
            print(totalsession)

        parent=session[0]
        child=session[1]

        # switch to child window
        driver.switch_to.window(child)

        # get the text of child window
        i=driver.find_element(By.XPATH,".//p[text()='Text within the pop up window']")
        data=i.text
        print(data)
        time.sleep(5)
        # close the child window
        driver.find_element(By.XPATH,".//p[text()='Close the Window']").click()
        time.sleep(5)

        #switch to parent window
        driver.switch_to.window(parent)

        # click the link in the parent window
        driver.find_element(By.ID,'secondajaxbutton').click()
        time.sleep(10)

r=Test_MultiWindowTest()
r.test_multiWindowTest()