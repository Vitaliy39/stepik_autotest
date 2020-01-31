from selenium import webdriver
import time
import os

link="http://suninjuly.github.io/file_input.html"

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_name("firstname")
    lastName = browser.find_element_by_name("lastname")
    eMail = browser.find_element_by_name("email")
    send = browser.find_element_by_id("file")
    name.send_keys("Ivan")
    lastName.send_keys("Ivanov")
    eMail.send_keys("email@email.com")
    send.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()