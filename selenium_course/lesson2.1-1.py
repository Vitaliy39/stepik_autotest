from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    #x_element = browser.find_element_by_id("input_value")
    #x=x_element.text
    y=calc(float(x))
    inputX = browser.find_element_by_id("answer")
    inputX.send_keys(str(y))
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
    