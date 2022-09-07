import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    res = calc(int(x))
    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()
