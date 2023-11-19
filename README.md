# Google forms
Use this code to fill in a google form.

You can also use this to automate any browser task.

Backstory
---------------------------
When virtual learning started due to covid, we had a google form to fill in for attendance. At that time, I felt that it was pointless to fill-in and submit the same form everyday. So then, I decided to use python and automate this task. When I first started this, it only worked with 1 browser. When I tested it on a differet browser, I realized that it had performed a bit differently. Now it has support for 3 different browsers.

Before using the code, note that selemium has been updated and xpaths are used differently.
Now you would probably use

```py
from selenium.webdriver.common.by import By
...
driver.find_element(By.XPATH, '//*[@id="Email"]')
```



Instructions
---------------------------  
   1.  Download [Python](https://www.python.org/downloads/) along with pip (you will need to do this manually during the installation of python)
   2.  Open cmd (command prompt) and type `pip install selenium` 
   3.  Download any code editor that can run python. I use [VS code](https://code.visualstudio.com/) with a [python extension](https://code.visualstudio.com/docs/languages/python).
   4.  Download [geckodriver (Mozilla Firefox)](https://github.com/mozilla/geckodriver/releases), [chromedriver (Chrome)](https://chromedriver.chromium.org/downloads) or [msedgedriver (Microsoft Edge)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it in some directory.
   5.  After you install a driver go to the corresponding folder
   6.  Download the files
   7.  Edit `config.json` accordingly 
   8.  You might need to change the email in the `main.py` file to add a number depending on how your email systems work
for example from:  
`{firstName}.{lastName}@gmail.com` to `{firstName}.{lastName}7@gmail.com`<br>
    you might need to change the email depending on the form and your domain.
   9.  Run the `main.py` file

Notes
------------------------------------------  

 - You could open the file with a normal text editor, and run the file from the command line.

 - If you want to use a specific driver, you need the corresponding browser.

To find an elements xpath:

First open the inspector
![step 1](https://github.com/Kev-in123/google-forms/assets/75402062/d86e3f4e-e513-415e-9039-486b994d9c95)
Then select the element
![step 2](https://github.com/Kev-in123/google-forms/assets/75402062/669a5213-4923-487f-947e-677430ac6178)
Finally right click, select copy, and select xpath
![step 3](https://github.com/Kev-in123/google-forms/assets/75402062/5290eb88-be48-4200-ab8a-616f23a759e7)


All the xpaths were fetched from Google Chrome but the examples use Mozilla Firefox

###### haven't tested since last commit
