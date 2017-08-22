# READ ME! 
# developing asana crawler 

# importing selenium and bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import time

#여기선는 크롬 chrome driver사용한다.
driver = webdriver.Chrome('C:\chromedriver')

# wait time 5 sec for loading component
driver.implicitly_wait(3)

