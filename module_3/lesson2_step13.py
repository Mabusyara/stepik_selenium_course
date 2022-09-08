import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def try_registration(link: str):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        input3.send_keys("ivan@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # возвращаем появившееся сообщение
        return welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


class Test(unittest.TestCase):
    def test_first_link(self):
        check = try_registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual(check, "Congratulations! You have successfully registered!",
                         "Registration not completed")

    def test_second_link(self):
        check = try_registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual(check, "Congratulations! You have successfully registered!",
                         "Registration not completed")


if __name__ == "__main__":
    unittest.main()

