import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'empty_file.txt')           # добавляем к этому пути имя файла

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
    browser.find_element(By.NAME, "email").send_keys("ivan@mail.ru")

    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()