import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    chest_with_x = browser.find_element(By.ID, "treasure")
    x = chest_with_x.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
