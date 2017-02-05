
# coding: utf-8

# In[9]:

import os
import sys
import wget 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# In[46]:

links = ['http://videohost.site/play/y0mgnHcdyduX0M8/', 'http://videohost1.com/play/EEYV5Bmbdwj9ZDy/', 'http://hindimoviesonline.watch/wp-content/uploads/AroundTheWorld.html', 'http://hindimoviesonline.watch/wp-content/uploads/new.html', 'http://hindimoviesonline.watch/wp-content/uploads/TrendingNow.html']

driver = webdriver.Chrome()
for i in links:
    url = i
    driver.get(url)
    try:
        print(driver.find_element_by_tag_name('video').get_attribute('duration'))
    except:
        pass



