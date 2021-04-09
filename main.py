from selenium import webdriver # first 3 lines are used to import stuff
import time
from selenium.webdriver.common.keys import Keys

web = webdriver.Edge("C:\\msedgedriver.exe")
web.get('https://forms.gle/Fccr1YANeRW6Usfu5') # used for form link

id = 'student id' # this is your student id
passw = 'password' # this is your password

email='firstname.lastname@student.tdsb.on.ca' # this is your student email there might be a number

try:
  emailpath=web.find_element_by_xpath('//*[@id="identifierId"]') # uses "try... except..." to get the input box because you might get a different sign-in page (I found this problem before)
except:
  emailpath=web.find_element_by_xpath('//*[@id="Email"]')

emailpath.send_keys(email) # sends email
emailpath.send_keys(Keys.ENTER) # signs you in

time.sleep(1) # lets page load before continue running code or else error will occur
username_textbox = web.find_element_by_xpath('//*[@id="UserName"]') # this is your student id 
username_textbox.send_keys(id) # this is to send student id

password_textbox = web.find_element_by_xpath('//*[@id="Password"]') # this is your password 
password_textbox.send_keys(passw) # this is to send password
password_textbox.send_keys(Keys.ENTER) # used to send data above

# You might ask why not find the button and click it. aw login won't let my code click the login button but the enter key works

# the code below is determend on the form your teacher wants you to fill in but I will still explain the code below

time.sleep(3) # lets page load before continue running code or else error will occur 
idnum = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input') # used to find the textbox for your student id
idnum.send_keys(id) # this is to send you student id

firstName = 'First name' # this is your first name
first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input') # used to find the textbox for your first name
first.send_keys(firstName) # used to send first name

lastName = 'Last name' # this is your last name
last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input') # used to find the textbox for your last name
last.send_keys(lastName) # used to send last name

RadioCohort = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]') # used to find cohort dropdown menu
RadioCohort.click() # used to click and open cohort dropdown menu

Cohort= web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]') # used to find your cohort
Cohort.click() # used to select your cohort

Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span') # used to find submit button
Submit.click() # used to click submit button