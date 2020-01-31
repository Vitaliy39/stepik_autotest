from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value")
    answer = calc(float(x.text))
    myText = browser.find_element_by_id("answer")   
    myText.send_keys(str(answer)) 
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()