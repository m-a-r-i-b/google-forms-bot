


# Age
# 0 		18-30
# 1 		18 to 30
# 2 		31 to 40
# 3 		41 to 50
# 4 		51 to 60

# Gender
# 5 		Male
# 6 		Female

# Educational Background 
# 7 		Matriculation
# 8 		Intermediate
# 9 		Bachelors
# 10 		Masters
# 11 		Post-Masters

# Do you use banking services?
# 0 		Yes
# 1 		No

# Which banking method you use for making transactions?
# 0 		Conventional (Branch Banking)
# 1 		Digital Banking
# 2 		Both

# Share reasons for not using digital banking channel. 
# 0         Security Issues
# 1         Login Issues
# 2         Accessibility Issues
# 3         Difficult to Understand
# 4         Unavailability of Features
# 5         Poor UI/UX (Design Issues)
# 6         Other


from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

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

for x in range(25):
    browser.get("https://forms.gle/Th85Ck8pATHmtGsa7")

    # myElem = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'appsMaterialWizButtonPaperbuttonLabel')))
   
    # 
    # Landing Page 
    # 
    # time.sleep(2)
    nextBtn = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizButtonPaperbuttonLabel')))
    # nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[0].click()


    # 
    # Demographics 
    # 
    radioButtons = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')))

    # Age
    radioButtons[0].click()

    # Gender
    radioButtons[5].click()

    # Educational Background
    radioButtons[11].click()

    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[1].click()



    # Do you use banking services
    radioButtons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    radioButtons[0].click()

    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[1].click()



    #  Which banking method you use for making transactions
    radioButtons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    radioButtons[2].click()

    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[1].click()


    #  Which banking method you use for making transactions
    radioButtons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    radioButtons[1].click()
    radioButtons[6].click()
    radioButtons[11].click()

    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[1].click()




    #  Which banking method you use for making transactions
    radioButtons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    radioButtons[1].click()
    radioButtons[6].click()

    # ------------------------Next 
    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[1].click()

    # Share reasons for not using digital banking channel
    checkBoxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxEl")

    time.sleep(0.5) 
    checkBoxes[3].click()
    checkBoxes[4].click()
    checkBoxes[5].click()

    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[1].click()


    checkBoxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxEl")

    time.sleep(0.5) 
    checkBoxes[0].click()
    checkBoxes[1].click()
    checkBoxes[3].click()

    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[1].click()


    checkBoxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxEl")

    time.sleep(0.5) 
    checkBoxes[0].click()
    if bool(random.getrandbits(1)): 
        checkBoxes[1].click()
    if bool(random.getrandbits(1)): 
        checkBoxes[3].click()
    if bool(random.getrandbits(1)): 
        checkBoxes[4].click()
    if bool(random.getrandbits(1)): 
        checkBoxes[5].click()

    nextBtn = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    nextBtn[1].click()

    #  Which banking method you use for making transactions
    radioButtons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    radioButtons[0].click()
    radioButtons[3].click()


    # ------------------------ Submit
    submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    submitbutton[1].click()

    # Wait till submit is completed
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'freebirdFormviewerViewResponseConfirmationMessage')))


#browser.close()
