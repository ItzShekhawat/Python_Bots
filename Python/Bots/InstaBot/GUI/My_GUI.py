import tkinter as tk

from selenium import webdriver
import time
import random


# -------------------------------------------------------- Creating an instance ----------------------------
win  = tk.Tk()
win.geometry("350x300")                                   # --------Size-------------
#--------------------------------------------------------- Adding qualities to the windows -----------------

win.title("Instagram Bot for liks")                                        # Title
win.resizable(False , False)                                               # Telling him to not let anyone resize the x and y of the GUI
win.configure(background = "#feda77")
win.grid_columnconfigure(0, weight = 1)


def liketheshit():
    #time.sleep(1200)
    #---------------------------------------------------- Starting the web screen -------------------------------
    driver  = webdriver.Chrome()
    driver.get("https://www.instagram.com")
    time.sleep(2)
    count = 0 # For the controll
    maxLiks = 50
    #follow = False

    driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys("call_me_the_tall_king")
        #.send_keys(input_user.get())
    driver.find_element_by_xpath('//input[@name=\"password\"]')\
        .send_keys("Karni2000")
        #.send_keys(input_pass.get())
    time.sleep(4)
    driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')\
        .click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()
    time.sleep(2)

    print("Im logged in and ready to go")
    #---------------------------------------------------------------------------------------------------------------------------------

    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
        .send_keys("#body")
        #.send_keys(input_search.get())
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')\
        .click()
    time.sleep(2)
    print("Im on the posts")

    win.destroy()

    time.sleep(8)

    #------------------------------------------------- Time to like some posts ------------------------------------------
    # First click

    try:
        print("First option")

        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')\
            .click()
        time.sleep(3)


        """
        row_post = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]')
        links = row_post.find_element_by_tag_name('a')
        print("Link taken")
        driver.find_elements_by_tag_name(links)\
            .click()
        """

    except:
        print("Second option")
        """
        driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[4]/article/div/div/div/div[1]/a/div[1]/div[1]')\
            .click()
        time.sleep(3)"""


    #---------------------------------------------- Time  to chose some pics --------------------------------------
    """
    print("First Post cliked")
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')\
            .click()
    time.sleep(random.randint(3, 4))
    
    print("")
    print("First post skipped") 

    """

    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')\
                .click()
            print("Liked")
            count += 1
            print(count)
            time.sleep(random.randint(2, 4))

            for _ in range(random.randint(1, 10)):
                driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')\
                    .click()
                time.sleep(random.randint(2, 4))
            print("Went forward")
        except:
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')\
                .click()
            time.sleep(random.randint(3, 4))
        

        if count > maxLiks :
            print("Im done")  
            driver.close()   
            break

    
# -----------------------------------------GUI---------------------------------

user_Lable = tk.Label(win, text = "Username", font = ("Helvetica", 14), bg = "#FCAF45")
user_Lable.grid(row = 0 , column = 0, sticky = "N", padx = 50, pady = 8)

input_user = tk.Entry()
input_user.grid(row = 1, column = 0 , sticky = "WE", padx = 50, pady = 2)

pass_Lable = tk.Label(win, text = "Password", font = ("Helvetica", 14), bg = "#FCAF45")
pass_Lable.grid(row = 2 , column = 0, sticky = "N", padx = 50, pady = 8)

input_pass = tk.Entry()
input_pass.grid(row = 3, column = 0 , sticky = "WE", padx = 50, pady = 2)

search_Lable = tk.Label(win, text = "Hashtag or Follower", font = ("Helvetica", 14), bg = "#FCAF45")
search_Lable.grid(row = 4 , column = 0, sticky = "N", padx = 50, pady = 8)

input_search = tk.Entry()
input_search.grid(row = 5, column = 0 , sticky = "WE", padx = 50, pady = 2)

btn = tk.Button(win, text = "Let's Like IT", font = ("Monaco", 20), bg  = "#dd2a7b", command = liketheshit)
btn.grid(row = 6, column = 0, sticky = "N", padx = 0 , pady = 10)



if __name__ == '__main__':
    
    win.mainloop()                                          # To start all the setting for the GUI
    










