from selenium import webdriver
from time import sleep

class TelloBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver  = webdriver.Chrome()
        self.driver.get("https://tellonym.me")
        sleep(3)

    try:
        
        def login(self):
            cookie = self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/a[2]/span")
            cookie.click()
            print("Cookie Accettato")
            logBtn = self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[2]/div[3]/div")
            logBtn.click()
            sleep(1)
            user = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div/div[2]/form/div[1]/input')
            user.send_keys(self.username)
            passw = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div/div[2]/form/div[2]/input')
            passw.send_keys(self.username)
            sleep(1)
            submit = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div/div[2]/form/button/div/div')
            submit.click()
            sleep(3)
            print("We Are In")

    except:
        print("Login went Wrong")
        



tello = TelloBot("Username_0029", "Karni1973")
tello.login()


