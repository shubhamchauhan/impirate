import os
import sys
import wget 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "http://www.hdmovieswatch.net/watch-dangal-2016-full-movie-online-for-dvdrip/"

driver = webdriver.Chrome()
driver.get(url)

WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "video")))
src = driver.page_source
print(src)