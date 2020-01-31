from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    myPrice="$100"
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    x = browser.find_element_by_id("input_value")
    answer = calc(float(x.text))
    myText = browser.find_element_by_id("answer")   
    myText.send_keys(str(answer)) 
    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()