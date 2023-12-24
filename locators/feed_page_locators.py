from selenium.webdriver.common.by import By


class FeedPageLocators:
    NEWEST_ORDER_IN_FEED_LIST = (By.XPATH, "//ul[contains(@class, 'Order')]//li[contains(@class, 'list')]")
    ORDER_CARD = (By.XPATH, "//p[text()='Cостав']")
    ORDER_FEED_TEXT = (By.TAG_NAME, "h1")
    ORDER_ID_LIST = (By.XPATH, "//div[contains(@class,'Box')]/p[contains(@class,'digits')]")
    ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[contains(text(), 'время')]/following-sibling::p")
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[contains(text(), 'сегодня')]/following-sibling::p")
    ORDERS_IN_WORK_LIST = (By.XPATH, "//ul[contains(@class, 'Ready')]/li")
    NO_ORDERS_IN_WORK = (By.XPATH, "//li[text()='Все текущие заказы готовы!']")
