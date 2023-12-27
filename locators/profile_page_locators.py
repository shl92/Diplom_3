from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDERS_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    HISTORY_BOX = (By.XPATH, "//div[contains(@class, 'OrderHistory')]")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
