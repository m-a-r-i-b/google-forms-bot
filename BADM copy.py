


# Female      Male            Prefer not to say
# 0             1                 2

# Single      Married         Prefer not to say
# 3              4                 5

# 18-24       25-31           32-38       39-45       46 and above
# 6             7               8           9             10


# Matric      Intermediate    Under-graduate  Graduate        PhD
# 11              12               13              14         15

# Up to 40k   41k to 70k  71k to 100k     101k to 150k    150k and above      Prefer not to say
# 16             17         18                  19              20                   21





# I feel comfortable while using internet banking services.
# 0-4

# Using internet banking services is easy for me.
# 5-9

# I find all internet banking content understandable.
# 10-14

# I can use internet banking services without asking for help.
# 15-19

# I think the easy use of internet banking services makes it more useful.
# 20-24





# People whose opinions I value think that internet banking is useful.
# 0-4

# People who influence my behavior think that I should use internet banking.
# 5-9

# I most likely tend to benefits from others’ experience and their advice..
# 10-14

# The others’ opinions motivate me to use internet banking.
# 15-19

# People in my environment who use Internet banking services have a high profile
# 20-24






# Using internet banking gives me greater control over my financial issues.
# 0-4

# Using internet banking provides me with convenient access to my accounts.
# 5-9

# Using internet banking saves my time and enables me to do my banking activity quickly.
# 10-14

# Using internet banking enables me to utilize the bank’s services efficiently.
# 15-19





# The bank’s website can be accessed when needed – 24 hours/day, 7 days/week
# 0-4

# The bank’s web design and navigation makes it comfortable to conduct a transaction
# 5-9

# The bank’s website executes transactions quickly and efficiently
# 10-14

# There is evidence that the current security provided by the bank website is sufficient
# 15-19



# There is a chance to lose money if I use internet banking services.
# 0-4

# I am worried that third parties would steal my username and password.
# 5-9

# Fixing payments errors after using internet banking may require a long time Thus reducing the convenience of these services.
# 10-14

# Internet banking servers may not perform well and thus process payment incorrectly.
# 15-19

# I think that it would be risky if I use Internet banking
# 20-24




from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()

chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = { "popups": 1 }
option.experimental_options["prefs"] = chrome_prefs

option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
# option.add_experimental_option("excludeSwitches", ['disable-popup-blocking'])
# option.add_argument("--disable-popup-blocking")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
browser = webdriver.Chrome(executable_path='/home/marib/bin/chromedriver', options=option)

for x in range(10):
    browser.get("https://forms.gle/UvtYUeejoc1ELeYG9")

    # myElem = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'appsMaterialWizButtonPaperbuttonLabel')))
   
    # 
    # Landing Page 
    # 

    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # Use online banking - YES
    radioButtons[0].click()

    nextBtn = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizButtonPaperbuttonLabel')))
    nextBtn[0].click()

# 
    # Demographics
#  
    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # Gender
    time.sleep(1)
    radioButtons[1].click()

    # Marital Status
    time.sleep(1)
    radioButtons[4].click()

    # Age
    time.sleep(1)
    radioButtons[8].click()

    # Education
    time.sleep(1)
    radioButtons[12].click()

    # Income
    time.sleep(1)
    radioButtons[21].click()


    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[6].click()

# 
    # Ease of Use
# 
    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # I feel comfortable while using internet banking services.
    time.sleep(1)
    radioButtons[0].click()

    # Using internet banking services is easy for me.
    time.sleep(1)
    radioButtons[7].click()
    
    # I find all internet banking content understandable.
    time.sleep(1)
    radioButtons[12].click()
    
    # I can use internet banking services without asking for help.
    time.sleep(1)
    radioButtons[18].click()
    
    # I think the easy use of internet banking services makes it more useful.
    time.sleep(1)
    radioButtons[24].click()
    
    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[6].click()

# 
    # Subjective Norms
# 
    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # People whose opinions I value think that internet banking is useful..
    time.sleep(1)
    radioButtons[0].click()

    # People who influence my behavior think that I should use internet banking.
    time.sleep(1)
    radioButtons[7].click()
    
    # I most likely tend to benefits from others’ experience and their advice..
    time.sleep(1)
    radioButtons[12].click()
    
    # The others’ opinions motivate me to use internet banking.
    time.sleep(1)
    radioButtons[18].click()
    
    # People in my environment who use Internet banking services have a high profile
    time.sleep(1)
    radioButtons[24].click()
    
    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[6].click()

# 
    # Usefulness
# 
    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # Using internet banking gives me greater control over my financial issues.
    time.sleep(1)
    radioButtons[0].click()

    # Using internet banking provides me with convenient access to my accounts.
    time.sleep(1)
    radioButtons[7].click()
    
    # Using internet banking saves my time and enables me to do my banking activity quickly.
    time.sleep(1)
    radioButtons[12].click()
    
    # Using internet banking enables me to utilize the bank’s services efficiently.
    time.sleep(1)
    radioButtons[18].click()
    
    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[5].click()


# 
    # Web Features
# 
    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # The bank’s website can be accessed when needed – 24 hours/day, 7 days/week
    time.sleep(1)
    radioButtons[0].click()

    # The bank’s web design and navigation makes it comfortable to conduct a transaction
    time.sleep(1)
    radioButtons[7].click()
    
    # The bank’s website executes transactions quickly and efficiently
    time.sleep(1)
    radioButtons[12].click()
    
    # There is evidence that the current security provided by the bank website is sufficient
    time.sleep(1)
    radioButtons[18].click()
    
    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[5].click()



# 
    # Risk
# 
    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # There is a chance to lose money if I use internet banking services.
    time.sleep(1)
    radioButtons[0].click()

    # I am worried that third parties would steal my username and password.
    time.sleep(1)
    radioButtons[7].click()
    
    # Fixing payments errors after using internet banking may require a long time Thus reducing the convenience of these services.
    time.sleep(1)
    radioButtons[12].click()
    
    # Internet banking servers may not perform well and thus process payment incorrectly.
    time.sleep(1)
    radioButtons[18].click()
    
    # I think that it would be risky if I use Internet banking
    time.sleep(1)
    radioButtons[24].click()
    
    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[6].click()



# 
    # Adoption of online banking
# 
    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # The ability to access the internet at any time at work and at home
    time.sleep(1)
    radioButtons[0].click()

    # Documentary evidence is provided for all transactions performed online
    time.sleep(1)
    radioButtons[7].click()
    
    # The banks providing acceptable conditions and terms of service
    time.sleep(1)
    radioButtons[12].click()
    
    # Being able to trial doing banking transactions online before registering for the service
    time.sleep(1)
    radioButtons[18].click()
    
    # -----------------Submit 
    submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    submitbutton[5].click()

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'freebirdFormviewerViewResponseConfirmationMessage')))



#browser.close()
