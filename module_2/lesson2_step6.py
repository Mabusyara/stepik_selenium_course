import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element(By.ID, "input_value").text
    res = calc(int(x))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(res)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()