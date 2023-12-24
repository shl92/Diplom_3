from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    CREATE_BURGER_TEXT = (By.TAG_NAME, "h1")
    INGREDIENT_SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    INGREDIENT_BUN = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    LIST_OF_INGREDIENTS = (By.XPATH, "//h2[text()='Булки']/following-sibling::ul/")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_MODULE_WINDOW = (By.XPATH, "//div[contains(@class, 'container')]/button[contains(@class, 'close')]")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    FIELD_FOR_INGREDIENTS = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor')]")
    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@href, 'aaa72')]//p[contains(@class, 'counter')]")
    ORDER_STATUS = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    ORDER_ID = (By.XPATH, "//div[contains(@class, 'container')]//h2")
    ORDER_ID_DEFAULT = (By.XPATH, "//h2[text()='9999']")
