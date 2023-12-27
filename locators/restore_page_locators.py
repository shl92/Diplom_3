from selenium.webdriver.common.by import By


class RestorePageLocators:
    RECOVER_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_HIDE_BUTTON = (By.XPATH, "//div[contains(@class, 'action')]")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
