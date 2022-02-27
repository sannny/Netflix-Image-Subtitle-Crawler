from os import rename
import os
from selenium import webdriver
import time
#import chromedriver_binary
from selenium.webdriver.common import keys
from creds import *
from os_ss_refactoring import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC  
from selenium.common.exceptions import TimeoutException
from io import StringIO
import pyautogui
import math

# os.system('spoof-mac.py set 00:00:00:00:00:00 en0')
# chrome_options = webdriver.ChromeOptions()
# #chrome_options.add_argument("--incognito")
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# #chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# #chrome_options.add_experimental_option("useAutomationExtension", False)
# driver = webdriver.Chrome(chromeDriverPath,chrome_options=chrome_options)

def init(driver):
    
    driver.delete_all_cookies()
    full_Screen_browser(driver)
    driver.get(website)
    time.sleep(10)

    signin = getElement(driver,sign_in_xpath).click()
    time.sleep(5)


    email_field = getElement(driver,email_xpath).send_keys(email_id)
    pass_field = getElement(driver,pass_xpath).send_keys(password)
    signin_but = getElement(driver,signin_xpath).click()

    time.sleep(7)

    sann_profile = getElement(driver,sann_profile_xpath).click()

    time.sleep(5)

    driver.get(getSearchURL(series_name))

    time.sleep(5)

    # return list of movies:
    movies_div = driver.find_elements_by_class_name("title-card")
    movie_titles = [(div.find_element_by_css_selector('a').get_attribute("aria-label"),div.find_element_by_css_selector('a').get_attribute("href")) for div in movies_div]
    for title in movie_titles:
        if title[0].lower().replace(' ','') ==  series_name.lower().replace(' ',''):
            driver.get(title[1])
            break

    time.sleep(15)

    Play_Pause('pause',driver)


def getElement(driver,xPath):
    return driver.find_element_by_xpath(xPath)

def getSearchURL(series_name):
    url = 'https://netflix.com/search?q='+series_name.replace(" ","%")
    return url

def full_Screen_browser(webdriver):
    webdriver.maximize_window()

def enablePlayerDiagnostics(webdriver):
    #pyautogui.hotkey('ctrl','alt', 'shift', 'd')
    actions = ActionChains(webdriver)
    actions.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys('d').perform()

def enablePlayerControls(webdriver):
    actions = ActionChains(webdriver)
    actions.send_keys(Keys.END).perform()

def getPlayerDiagInfo(webdriver):
    js = """return document.evaluate('//html/body/div[4]/textarea', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value;"""
    return webdriver.execute_script(js)

def dumpPlayerDiagInfoDict(webdriver):
    s = StringIO(getPlayerDiagInfo(webdriver))
    d = dict()
    for line in s:
        if not line == '\n':
            kvlst = line.strip().split(': ')
            val = ''
            try:
                val = ': '.join(kvlst[1:]).strip()
            except:
                pass
            d[kvlst[0].strip()] = val
    return d

def player_info_close(driver):
    getElement(driver,player_info_close_button).click()

def getPlayerDiagnostics(webdriver):
    enablePlayerControls(webdriver)
    enablePlayerDiagnostics(webdriver)
    diags = dumpPlayerDiagInfoDict(webdriver)
    #time.sleep(3)
    player_info_close(webdriver)
    return diags

def play_pause_button(webdriver):
    pyautogui.moveTo(960,560)
    pyautogui.move(0,-200)
    pyautogui.click()
    #pyautogui.press('enter')
"""  actions = ActionChains(webdriver)"""    
"""     actions.send_keys(Keys.SPACE).perform()"""    

def Play_Pause(state,webdriver):
    
    diags = getPlayerDiagnostics(webdriver)
    
    if diags['Rendering state'] == 'Playing':
        if state != 'play':
            play_pause_button(webdriver)
    else:
        if state != 'pause':
            play_pause_button(webdriver)


def enable_disable_full_screen():
    pyautogui.click(x=750, y=600, clicks=2)


def Take_a_screenshot():
    pyautogui.hotkey('win', 'printscreen')


def move_to_beginning(webdriver):
    diags = getPlayerDiagnostics(webdriver)
    #no_of_backs = int(math.ceil(float(curr_position)/10))
    total_duration = diags['PlayerDuration']
    # if float(diags['Position']) <= 1.0:
    #     return total_duration
    # Play_Pause('pause',webdriver)
    # actions = ActionChains(webdriver)
    # while int(round(float(diags['Position']))) >= 1.0:
    #     pyautogui.move(0,1,1)
    #     actions.send_keys(Keys.ARROW_LEFT).perform()
    #     diags = getPlayerDiagnostics(webdriver)
    #     Play_Pause('pause',webdriver)
    #     time.sleep(2)
    # Play_Pause('pause',webdriver)
    pyautogui.moveTo(22,882)
    pyautogui.leftClick()
    return total_duration



def start_gathering(webdriver,total_duration):
    #enable_disable_full_screen()
    diags={}
    """
    diags = getPlayerDiagnostics(webdriver)
    checkRenderingState(webdriver,diags['Rendering state'])
    """
    rename = renaming()
    rename.clean_dir()
    while float(diags.get('Position',-1)) <= total_duration:
        Play_Pause('play',webdriver)
        #time.sleep(1.5)
        Play_Pause('pause',webdriver)
        
        diags = getPlayerDiagnostics(webdriver)
        #Play_Pause('pause',webdriver)
        
        Take_a_screenshot()
        NN = newName(diags['Position'])
        rename.__main__(NN) 
       

def initialize(driver):
    #time.sleep(5)
    total_duration = move_to_beginning(driver)
    start_gathering(driver,total_duration)

    time.sleep(5)

"""time.sleep(3)
Play_Pause(driver)
driver.save_screenshot(img_path)
Play_Pause(driver)
time.sleep(3)
Play_Pause(driver)
driver.save_screenshot(img_path)"""
 
""" waitForPlayerControlsByClassName(driver)"""

#driver.quit()







