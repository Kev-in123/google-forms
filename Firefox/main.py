from utils import get_data
from FillForm import fillForm
from selenium import webdriver

user = get_data()
data = {
  "web" : webdriver.Firefox(executable_path=user["dir"]),
  "_id" : user["id"],
  "fName" : user["first"],
  "lName" : user["last"],
  "passw" : user["password"],
  "email" : f"{user['first']}.{user['last']}@gmail.com, # there might be a number after the last name
  "link" : user['link']
}

f = fillForm(**data)
f.start()


