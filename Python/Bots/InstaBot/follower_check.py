from selenium import webdriver
import time
import random





class InstaBot :
    def __init__(self, username, pw):
        self.username = username
        self.pw = pw
        self.hashtagFind = "#edits"  #Hastag You want to liks
        self.maxliks = 2                #Numbers of likes 
        



        self.driver  = webdriver.Chrome()
        self.driver.get("https://www.instagram.com")
        time.sleep(2)
        self.count = 0 # For the controll
        


    def loging(self):

        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(self.pw)
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")\
            .click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        time.sleep(2)

    def checkFollow(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')\
            .click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[contains(@href, "/following")]')\
            .click()
        time.sleep(2)


    def search(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
            .send_keys(self.hashtagFind)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')\
            .click()
        time.sleep(2)
        print("Im on the posts")

        time.sleep(5)

        try:
            print("First option")
            row_post = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]')
            links = row_post.find_element_by_tag_name('a')
            print("Link taken")
            self.driver.find_elements_by_tag_name(links)\
                .click()
            
        except:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')\
                .click()
            time.sleep(5)


        
        print("First Post cliked")
        
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')\
            .click()
        time.sleep(random.randint(4, 10))

        print("First Skip")

        while True:
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')\
                    .click()
                print("Liked")
                self.count += 1
                print(self.count)
                time.sleep(random.randint(3, 9))

                for _ in range(random.randint(1, 5)):
                    self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')\
                        .click()
                    time.sleep(random.randint(4, 6))
            except:
                self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')\
                    .click()
                time.sleep(random.randint(4, 6))



            if self.count > self.maxliks :
                print("Im done")     
                break
            


    def closeChrome(self):
        self.driver.close()


if __name__ == "__main__":
    
    kevinAcc = InstaBot("call_me_the_tall_king","Karni2000")
    kevinAcc.loging()
    kevinAcc.search()
    #kevinAcc.checkFollow()