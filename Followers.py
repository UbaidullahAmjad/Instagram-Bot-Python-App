# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:42:46 2020

@author: Ali
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import xlsxwriter
#from instabot import Bot 

#bot = Bot() 



class InstagramBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    
    
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        #login_button.click()
        #time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def getUsersFollowers(self):
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div').click()
                time.sleep(2)
                # Workbook() takes one, non-optional, argument  
                # which is the filename that we want to create. 
                #workbook = xlsxwriter.Workbook('links.xlsx') 
                  
                # The workbook object is then used to add new  
                # worksheet via the add_worksheet() method. 
                #worksheet = workbook.add_worksheet() 
                
                UserIds=[]
                #column=0
                #find_href = self.driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/div[1]/a')
                find_href = self.driver.find_elements_by_class_name('FPmhX')
                for my_href in find_href:
                    #print(my_href.get_attribute("href"))
                    # write operation perform 
                    time.sleep(1)
                    UserIds.append(my_href.get_attribute("title")) 
                  
                    # incrementing the value of row by one 
                    # with each iteratons. 
                    
                      
                #workbook.close() 
                print(UserIds)
                print("Saved successfully")
                time.sleep(5)
                self.driver.implicitly_wait(5)
                self.driver.close()
                #time.sleep(5)
                #bot.login(username = "usmanaslam406",password = "usman11?") 
                #bot.follow(UserIds)
                


if __name__ == "__main__":

    username = "usmanaslam406"
    password = "Usman11?"

    ig = InstagramBot(username, password)
    ig.login()
    time.sleep(5)
    ig.driver.implicitly_wait(2)
    ig.getUsersFollowers()