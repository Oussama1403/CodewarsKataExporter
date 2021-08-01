from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import time

with open('setup.json') as fin:
    setup = json.load(fin)

#driver_path = '/usr/bin/geckodriver'

#brave_path = '/usr/bin/brave-browser-stable'
#option = webdriver.ChromeOptions()
#option.binary_location = brave_path


driver = webdriver.Firefox(firefox_profile="/home/oussama/.mozilla/firefox/joldrw80.default-release")
#url = driver.command_executor._url
#session_id = driver.session_id
#driver = webdriver.Remote(command_executor=url,desired_capabilities={})
#driver.close()
#driver.session_id = session_id

driver.get("https://www.codewars.com/")

#usernameElem = driver.find_element_by_id("user_email")
#passwordElem = driver.find_element_by_id("user_password")

#usernameElem.send_keys(setup['codewars']['email'])
#passwordElem.send_keys(setup['codewars']['password'])

#driver.find_element_by_xpath("//button[1]").click()
driver.find_element_by_xpath("//div[@class='profile-pic mr-0']/img[1]").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Solutions")))
driver.find_element_by_link_text('Solutions').click()
time.sleep(5)

#nReloads = setup['reloads_in_browser']

elem = driver.find_element_by_tag_name("body")

#for _ in range(nReloads):
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(4)
elem.send_keys(Keys.PAGE_UP)
time.sleep(2)

with open('source.html', 'w') as fin:
    fin.write(driver.page_source)

driver.close()
