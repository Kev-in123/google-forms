from selenium import webdriver # first 3 lines are used to import stuff
import time, schedule
from selenium.webdriver.common.keys import Keys

# defines a function so its easier to use
def attendance():
  web = webdriver.Edge("C:\\msedgedriver.exe" ) # used to open chrome double '\' to specify its a path
  web.get('https://forms.gle/Fccr1YANeRW6Usfu5') # used for form link

  id = 'student id' # this is your student id
  passw = 'password' # this is your password

  email='firstname.lastname@student.tdsb.on.ca' # this is your student email there might be a number

  try:
    emailpath=web.find_element_by_xpath('//*[@id="identifierId"]') # uses "try... except..." to get the input box because you might get a different sign-in page (I found this problem before)
  except:
    emailpath=web.find_element_by_xpath('//*[@id="Email"]')

  emailpath.send_keys(email) # sends email
  emailpath.send_keys(Keys.ENTER) # signs you in # used to click submit button

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

  Cohort= web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]') # used to find your cohort
  Cohort.click() # used to select your cohort

  Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span') # used to find submit button
  Submit.click() # used to click submit button
# to check if the form submission wwas successful
  time.sleep(2)
  try:
    web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    print("Form submitted successfully ")
  except:
    print("Unable to submit form")
# to schedule code
# note: It uses 24 hour local (device) time and if its before 12:00 you must add a zero at the front (shown below)
while True: # while loop so it runs every day instead of once at that time
  schedule.every().day.at("08:45").do(attendance)