from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.get("http://unlimitedmailinglists.com/site/auth/login.asp")
driver.find_element_by_name("Email").send_keys("dmamann@aol.com")
driver.find_element_by_name("Password").send_keys("Passc0de")
driver.find_element_by_css_selector("input[alt=Submit]").click()
driver.find_element_by_link_text('Dashboard').click()

links=driver.find_elements_by_tag_name('a')

for i in range(11,len(links)-3):
    if (i-11)%3==0:
        links[i].click()

time.sleep(15)

driver.close()