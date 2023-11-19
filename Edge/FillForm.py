import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class fillForm:
    def __init__(self, web, _id, fName, lName, passw, email, link):
        self.web = web
        self._id = _id
        self.fName = fName
        self.lName = lName
        self.passw = passw
        self.email = email
        self.link = link
    
    def login(self):
        self.web.get(self.link)
        try:
            emailpath = self.find('//*[@id="identifierId"]')

        except:
            emailpath = self.find('//*[@id="Email"]')
          
        emailpath.send_keys(self.email)
        emailpath.send_keys(Keys.ENTER)

        username_textbox = self.find('//*[@id="UserName"]')
        username_textbox.send_keys(self._id)

        password_textbox = self.find('//*[@id="Password"]')
        password_textbox.send_keys(self.passw)
        password_textbox.send_keys(Keys.ENTER)

    def fill(self):
        idnum = self.find('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        idnum.click()
        idnum.send_keys(self._id)

        first = self.find('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        first.send_keys(self.fName)

        last = self.find('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        last.send_keys(self.lName)

        RadioCohort = self.find('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        RadioCohort.click()

        Cohort = self.find('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]')
        Cohort.click()

    def submit(self):
        Submit = self.find('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
        Submit.click()

    def find(self, path):
        while True:
            try:
                return self.web.find_element_by_xpath(path)
            except selenium.common.exceptions.NoSuchElementException:
                time.sleep(0.1)


    def start(self):
        self.login()
        self.fill()
        self.submit()
