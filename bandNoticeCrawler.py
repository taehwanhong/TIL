# READ ME! 
# developing band notice crawler 

# importing selenium and bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import time

#여기선는 크롬 chrome driver사용한다.
driver = webdriver.Chrome('C:\chromedriver')

# wait time 5 sec for loading component
driver.implicitly_wait(3)

# direct a url(naver band)
driver.get('https://auth.band.us/login_page?next_url=http%3A%2F%2Fband.us%2Fband%2F67489377')
# redirect to login page
driver.find_element_by_xpath('//*[@id="login_list"]/li[4]').click()

# service login for naver(band)
driver.find_element_by_name('id').send_keys('$$$$$$$$')
driver.find_element_by_name('pw').send_keys('########')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

#find a node for notice and click
driver.find_element_by_class_name('notice').click()
time.sleep(1)
driver.find_element_by_class_name('prevComment').click()
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notice = soup.select('div.commentBody > div.cont > p.txt')

for n in notice:
    print(n.text.strip())