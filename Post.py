# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:51:14 2020

@author: Ali
"""

from instabot import Bot 

bot = Bot() 


bot.login(username = "usmanaslam406",password = "usman11?") 



c="C:\\Users\\Ali\\Desktop\\InstaBot\\Test\\1.jpg"

bot.upload_photo(c, caption="Here It is #software") 

