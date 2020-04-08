from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\chromedriver_win32\geckodriver.exe")

wait = WebDriverWait(driver, 20)

driver.get("http://unlimitedmailinglists.com/site/auth/login.asp")
driver.find_element_by_name("Email").send_keys("dmamann@aol.com")
driver.find_element_by_name("Password").send_keys("Passc0de")
driver.find_element_by_css_selector("input[alt=Submit]").click()
m=1
i='Q'
#a='C' #used for age
#j='1'
#k=8
for k in range(1,26):
    #if k==4 or k==8 or k==9 or k==46 or k==47 or k==50 or k==51 or k==12 or k==13 or k==2 or k==17 or k==19 or k==20 or k==25 or k==42:
        #continue
#for i in 'ABCDEFGHIJKLMNOPQRS':    #used for income
    for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='type1']")))
        driver.find_element_by_css_selector("input[value=C]").click()
        dp = Select(driver.find_element_by_name("statecode"))  # choosing drop down box
        dp.select_by_index(k)  # Selecting State
        driver.find_element_by_id("sb3").click()  # CLICKING ON FILTERs
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='gender']")))
        #driver.find_element_by_css_selector("input[value=F]").click()
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='age']")))
        #driver.find_element_by_xpath("//*[@id='age'][@value='C']").click()#USED FOR AGE
        #driver.find_element_by_xpath("//*[@id='age'][@value='D']").click()#USED FOR AGE
        #driver.find_element_by_xpath("//*[@id='age'][@value='G']").click()#USED FOR AGE
        #driver.find_element_by_xpath("//*[@id='age'][@value='H']").click()#USED FOR AGE
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='Birth_Month']")))
        driver.find_element_by_xpath("//*[@id='Birth_Month'][@value='" + j + "']").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='income']")))
        driver.find_element_by_xpath("//*[@id='income'][@value='" + i + "']").click()
        driver.find_element_by_xpath("//*[@id='creditRating'][@value='B']").click()#credit score
        #driver.find_element_by_xpath("//*[@id='creditRating'][@value='E']").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sb4']")))
        driver.find_element_by_id("sb4").click()  # CLICKING ON DOWNLOAD
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='DownloadDescription']")))
        driver.find_element_by_id("DownloadDescription").send_keys(m)
        m += 1
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sb5']")))
        driver.find_element_by_id("sb5").click()  # CLICKING ON START DOWNLOAD
        driver.find_element_by_link_text('Search').click()

time.sleep(1)
driver.close()

#for i in 'ABCDEFGHIJKLMNOPQRS':
#    for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:

#        driver.find_element_by_css_selector("input[value=C]").click()
#        dp = Select(driver.find_element_by_name("statecode"))  # choosing drop down box
#        dp.select_by_index(1)  # Selecting State
#        driver.find_element_by_id("sb3").click()  # CLICKING ON FILTERs
#        driver.find_element_by_css_selector("input[value=F]").click()
#        driver.find_element_by_xpath("//*[@id='Birth_Month'][@value='"+ j +"']").click()
#        driver.find_element_by_xpath("//*[@id='income'][@value='"+ i +"']").click()
#        driver.find_element_by_id("sb4").click()  # CLICKING ON DOWNLOAD
#        driver.find_element_by_id("sb5").click()  # CLICKING ON START DOWNLOAD
#        driver.find_element_by_link_text('Search').click()