import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    browser.find_element(By.TAG_NAME, "button").click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x = int(browser.find_element(By.ID, "input_value").text)
    res = calc(x)

    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()
