import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Exercise:
    def exercise(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\mohan\\Downloads\\driver\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Main Window
        driver.get("https://demoqa.com/browser-windows")

        driver.find_element(By.ID, 'tabButton').click()

        a=driver.window_handles

        for i in a:
            print(i)

        parent=a[0]
        child=a[1]

        print("Before switching ")
        data=driver.title
        print("parent window title----",data)

        # switch to Child window
        driver.switch_to.window(child)
        print("after switching")
        c1=driver.title
        print("child window title---",c1)

        c2=driver.find_element(By.XPATH,".//h1[text()='This is a sample page']")
        print("Child Window Text____",c2.text)

        driver.switch_to.default_content()


        print("switching to parent window")
        driver.switch_to.window(parent)
        driver.find_element(By.ID,'windowButton').click()

        second=driver.window_handles

        for i in second:
            print(i)

        g_parent=second[0]
        g_child=second[1]
        g_children=second[2]

        print("Switching to the new window")
        driver.switch_to.window(g_children)
        a1=driver.find_element(By.ID,'sampleHeading')
        print("newly opened child window--------",a1.text)

        print("switching to parent window")
        driver.switch_to.window(parent)
        driver.find_element(By.ID,'messageWindowButton').click()

        j=driver.window_handles

        for x in j:
            print(x)

        gg_parent=j[0]
        gg_child=j[1]
        gg_childrens=j[2]
        ggg_son=j[3]

        print("Switching to the new window message")
        driver.switch_to.window(ggg_son)
        #driver.find_element(By.XPATH,".//body[contains(text(),'Knowledge')]")
        t=driver.title
        print("new window message title is ",t)


        time.sleep(10)

c=Exercise()
c.exercise()