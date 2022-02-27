import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from Web_ScreenShoter import *
import os
from selenium import webdriver

scenarios('D:\\linux\\scratches\\Netflix_image_subtitle_crawler\\Web_ScreenShoter_feat.feature')
files = []

@pytest.fixture
def browser():
    global driver
    os.system('spoof-mac.py set 00:00:00:00:00:00 en0')
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chromeDriverPath,chrome_options=chrome_options)
    yield
    driver.quit()

@given('Sign in and start the episode')
def given(browser):
    init(driver)

@when('Restart the episode')
def when_one(browser):
    total_duration = move_to_beginning(driver)

@then('Compare the slider time to be less than 1 sec')
def then_one(browser):
    assert(float(getPlayerDiagnostics(driver)['Position'])<=1.0)


@when('Start gathering data')
def when_two(browser):
    diags={}
    """
    diags = getPlayerDiagnostics(webdriver)
    checkRenderingState(webdriver,diags['Rendering state'])
    """
    rename = renaming()
    rename.clean_dir()
    while float(diags.get('Position',-1)) <= 10.0:
        Play_Pause('play',driver)
        Play_Pause('pause',driver)
        
        diags = getPlayerDiagnostics(driver)
        #Play_Pause('pause',driver)
        
        Take_a_screenshot()
        NN = newName(diags['Position'])
        rename.__main__(NN)
        if NN.getNewName()!='0_001':
            files.append(''.join([str(NN.getNewName()),'.png']))

@then('Compare the list of screenshots files')
def then_two(browser):
    rename = renaming()
    rename.switch_to_ss_dir()
    our_files = rename.list_all_files()
    print('Our Files:')
    for file in our_files:
        print(file)
    print('Files arr:')
    for file in files:
        print(file)
    assert(set(our_files)==set(files))

