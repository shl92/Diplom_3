from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")  # Поле для ввода e-mail
    PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле для ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа
