
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


class Browse(object):
    
    def run(self, urls):
        results = []
        driver = webdriver.Chrome()
        for i in urls:
            url = i
            driver.get(url)
            try:
                p = driver.find_element_by_tag_name('video').get_attribute('duration')
                results.append([url,p])
            except:
                pass
        return(results)



