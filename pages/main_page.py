import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver import ActionChains


class MainPage(BasePage):
    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_profile_button(self):
        self.find_element_and_click(MainPageLocators.PROFILE)

    @allure.step("Нажать на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.find_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажать на кнопку 'Лента заказов'")
    def click_orders_feed_button(self):
        self.is_element_present(MainPageLocators.ORDER_FEED_BUTTON)
        self.find_element(MainPageLocators.ORDER_FEED_BUTTON).click()

    @allure.step("Нажать на ингридиент")
    def ingredient_click(self):
        self.find_element_and_click(MainPageLocators.INGREDIENT_SAUCE)

    @allure.step("Нажать на кнопку закрытия карточки ингридиента")
    def close_ingredient_card(self):
        self.find_element_and_click(MainPageLocators.CLOSE_MODULE_WINDOW)

    @allure.step("Выбрать ингридиент")
    def choose_ingredient(self, ingredient_locator):
        return self.find_element(ingredient_locator)

    @allure.step("Выбрать поле конструктора заказа для ингридиента")
    def choose_field_for_ingredients(self):
        return self.find_element(MainPageLocators.FIELD_FOR_INGREDIENTS)

    @allure.step("Добавить ингридиент в поле конструктора заказа")
    def add_ingredient_to_order(self, ingredient_locator):
        ingredient = self.choose_ingredient(ingredient_locator)
        field = self.choose_field_for_ingredients()
        action = ActionChains(self.driver)
        action.drag_and_drop(ingredient, field).perform()

    @allure.step("Нажать на кнопку создания заказа")
    def create_order_button_click(self):
        self.find_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Получить ID созданного заказа")
    def get_order_id(self):
        self.is_element_no_more_located(MainPageLocators.ORDER_ID_DEFAULT)
        return self.find_element(MainPageLocators.ORDER_ID).text

    @allure.step("Закрыть карточку заказа")
    def close_order_card(self):
        self.find_element_and_click(MainPageLocators.CLOSE_MODULE_WINDOW)

    @allure.step("Создать заказ")
    def create_order(self):
        self.open_page()
        self.add_ingredient_to_order(MainPageLocators.INGREDIENT_BUN)
        self.add_ingredient_to_order(MainPageLocators.INGREDIENT_SAUCE)
        self.create_order_button_click()
        order_id = self.get_order_id()
        self.close_order_card()
        return int(order_id)

    @allure.step("Проверка перехода на главную страницу - наличие текста 'Соберите бургер'")
    def check_text_create_burger_on_main_page(self):
        assert self.is_element_displayed_on_page(MainPageLocators.CREATE_BURGER_TEXT), ("Текст 'Соберите бургер' не "
                                                                                        "найден на главной странице "
                                                                                        "сайта")

    @allure.step("Проверка закрытия карточки ингридиента - отсутствие текста 'Детали ингридиента'")
    def check_ingredient_card_is_closed(self):
        assert self.is_element_no_more_located(MainPageLocators.INGREDIENT_DETAILS), ("Карточка ингридиента не "
                                                                                      "закрылась, текст 'Детали "
                                                                                      "ингридиента' по прежнему "
                                                                                      "присутствует на странице")

    @allure.step("Проверка открытия карточки ингридиента - наличие текста 'Детали ингредиента'")
    def check_ingredient_card_opened(self):
        assert self.is_element_displayed_on_page(MainPageLocators.INGREDIENT_DETAILS), ("Карточка деталей ингридиента "
                                                                                        "не открылась - текст 'Детали "
                                                                                        "ингредиента' не найден")

    @allure.step("Проверка счетчика ингридиента")
    def check_ingredient_counter_number(self):
        counter_number = self.find_element(MainPageLocators.INGREDIENT_COUNTER).text
        assert counter_number == '1', (f"Количество ингредиента не соответствует. Ожидаемое: 1, "
                                       f"фактическое: {counter_number}")

    @allure.step("Проверка создания заказа - наличие текста 'Ваш заказ начали готовить'")
    def check_order_status(self):
        status = self.find_element(MainPageLocators.ORDER_STATUS).text
        assert status == "Ваш заказ начали готовить", "Заказ не оформлен, текст 'Ваш заказ начали готовить' не найден"
