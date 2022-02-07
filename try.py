"""from HTMLParser import HTMLParser
hp = HTMLParser()
text = u"७ ]। ०-० ०  [>075फ॥70 66 0695    यह तुम्हारे लिए है, है न?"
hp.unescape(text)
print(hp.unescape(text))
hp.unescape(text).split()
print(" ".join(hp.unescape(text).split()))"""

import pyautogui
import datetime

def eta():
    start = datetime.datetime.now()
    width, height = pyautogui.size()[0], pyautogui.size()[1]
    curr_height = pyautogui.position()[1]
    if height/2 >= curr_height:
        pyautogui.move(0,100)
    else:
        pyautogui.move(0,-200)
    pyautogui.click()
    end = datetime.datetime.now()
    eta = end-start
    print(eta)

pyautogui.moveTo(960,560)
eta()