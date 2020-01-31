from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")
    answer = int(x.text)+int(y.text)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(answer))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()