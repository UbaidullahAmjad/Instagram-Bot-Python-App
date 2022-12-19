# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:55:50 2020

@author: Ali
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def NonFollowers(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep()
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
        #time.sleep(5)
        #bot.login(username = "usmanaslam406",password = "usman11?") 
        #bot.Unfollow(UserIds)


if __name__ == "__main__":

    username = "usmanaslam406"
    password = "Usman11?"

    ig = InstagramBot(username, password)
    ig.login()
    time.sleep(5)
    ig.driver.implicitly_wait(2)
    ig.NonFollowers()