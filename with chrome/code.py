from selenium import webdriver # first 4 lines are used to open links and send data
import time
from selenium.webdriver.common.keys import Keys

web = webdriver.Chrome("C:\\chromedriver.exe" ) # used to open chrome double '\' to specify its a path
web.get('https://forms.gle/Fccr1YANeRW6Usfu5') # used for form link

id = 'student id' # this is your student id
passw = 'password' # this is your password

email='firstname.lastname@student.tdsb.on.ca' # this is your student email there might be a number
emailpath=web.find_element_by_xpath('//*[@id="identifierId"]') # used to find email textbox
emailpath.send_keys(email) # used to send email

Submit_Mail = web.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]') # used to find submit button
Submit_Mail.click() # used to click submit button

time.sleep(1) # lets page load before continue running code or else error will occur
username_textbox = web.find_element_by_xpath('//*[@id="UserName"]') # this is your student id 
username_textbox.send_keys(id) # this is to send student id

password_textbox = web.find_element_by_xpath('//*[@id="Password"]') # this is your password 
password_textbox.send_keys(passw) # this is to send password
password_textbox.send_keys(Keys.ENTER) # used to send data above

# You might ask why not find the button and click it. aw login won't let my code click the login button but the enter key works

time.sleep(1) # lets page load before continue running code or else error will occur 
confirm=web.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]') # used to find confirm button
confirm.click() #used to click confirm button

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

time.sleep(2) # lets options load before continue running code or else error will occur 
Cohort= web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]') # used to find your cohort
Cohort.click() # used to select your cohort

time.sleep(2) # I explained this too many times so I'll let you figure out this one 
Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span') # used to find submit button
Submit.click() # used to click submit button
