import time
from utils import get_data as user
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

web = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
web.get("https://forms.gle/Fccr1YANeRW6Usfu5")

id_ = user['id']
passw = user['password']
firstName = user['first']
lastName = user['last']

email=f'{firstName}.{lastName}@student.tdsb.on.ca'

try:
  emailpath=web.find_element_by_xpath('//*[@id="identifierId"]')
except:
  emailpath=web.find_element_by_xpath('//*[@id="Email"]')
  
emailpath.send_keys(email)
emailpath.send_keys(Keys.ENTER)

while True:
  try:
    username_textbox = web.find_element_by_xpath('//*[@id="UserName"]')
    break
  except selenium.common.exceptions.NoSuchElementException:
    time.sleep(0.1)

username_textbox.send_keys(id)

password_textbox = web.find_element_by_xpath('//*[@id="Password"]')
password_textbox.send_keys(passw)
password_textbox.send_keys(Keys.ENTER)


while True:
  try:
    idnum = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    break
  except selenium.common.exceptions.NoSuchElementException:
    time.sleep(0.1)

idnum.send_keys(id)

first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(firstName)

last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(lastName)
RadioCohort = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]')
RadioCohort.click()

Cohort= web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]')
Cohort.click()

Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()
