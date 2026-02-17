from selenium.webdriver.common.by import By
from Page.base_page import BasePage

class LoginPage(BasePage):
    # Локаторы
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")  # локатор ошибки

    # Открыть страницу
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    # Метод логина
    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    # Метод для получения текста ошибки
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text
