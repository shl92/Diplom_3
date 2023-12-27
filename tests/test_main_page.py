import allure
from pages.main_page import MainPage
from data.urls import URLS
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage


@allure.feature("Проверка функционала главной страницы сайта")
class TestMainPage:
    @allure.title("Проверка перехода на главную страницу по кнопке 'Конструктор'")
    @allure.description("Логин в систему, переходим на страницу ленты заказов, нажимаем на кнопку 'Конструктор', "
                        "проверяем наличие текста 'Собери бургер' на главной странице сайта")
    def test_constructor_button_click(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_orders_feed_button()
        main_page.click_constructor_button()
        main_page.check_text_create_burger_on_main_page()

    @allure.title("Проверка перехода на ленту заказов по кнопке 'Лента заказов'")
    @allure.description("Логин в систему, нажимаем на кнопку 'Лента заказов', проверяем наличие текста 'Лента "
                        "заказов' на странице ленты заказов")
    def test_orders_feed_button_click(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_orders_feed_button()
        feed_page = FeedPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.check_text_order_feed_on_feed_page()

    @allure.title("Проверка появления всплывающего окна после клика на ингредиент")
    @allure.description("Логин в систему, нажимаем на ингридиент, проверяем наличие текста 'Детали ингридиента' в "
                        "открывшейся карточке")
    def test_open_ingredient_card(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.ingredient_click()
        main_page.check_ingredient_card_opened()

    @allure.title("Проверка закрытия всплывающего окна деталей ингридиентов")
    @allure.description("Логин в систему, нажимаем на ингридиент, нажимаем на крестик для закрытия окна, проверяем "
                        "отсутствие текста 'Детали ингридиента' на странице")
    def test_close_ingredient_card(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.ingredient_click()
        main_page.close_ingredient_card()
        main_page.check_ingredient_card_is_closed()

    @allure.title("Проверка увеличения счетчика ингридиента при добавлении игридиента в заказ")
    @allure.description("Логин в систему, добавляем ингридиент в заказ, проверяем увеличение счетчика ингридиента")
    def test_increase_ingredient_counter(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.add_ingredient_to_order(MainPageLocators.INGREDIENT_SAUCE)
        main_page.check_ingredient_counter_number()

    @allure.title("Проверка возможности оформления заказа для залогиненного пользователя")
    @allure.description("Логин в систему, добавляем ингридиент в заказ, нажимаем на кнопку 'оформить заказ', "
                        "поверяем наличие текста 'Ваш заказ начали готовить'")
    def test_create_button_click(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.add_ingredient_to_order(MainPageLocators.INGREDIENT_BUN)
        main_page.create_order_button_click()
        main_page.check_order_status()
