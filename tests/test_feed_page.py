import allure
from pages.main_page import MainPage
from data.urls import URLS
from pages.feed_page import FeedPage
from pages.profle_page import ProfilePage


@allure.feature("Проверка функционала страницы Лента заказов")
class TestFeedPage:
    @allure.title("Проверка открытия окна деталей заказа при клике на заказ")
    @allure.description("Логин в систему, открытие страницы ленты заказов, клик на карточку с заказом, проверка "
                        "наличия текста 'Состав' во всплывающей карточке заказа")
    def test_open_order_card(self, driver, login_user):
        feed_page = FeedPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.open_page()
        feed_page.click_on_first_order_card()
        feed_page.check_order_card_opened()

    @allure.title("Проверка отображения заказов пользователя из истории заказов профиля на странице 'Лента заказов'")
    @allure.description("Логин в систему, создаем заказ, переходим в личный кабинет, кликаем на ссылку 'История "
                        "заказов', проверяем наличие созданного ID заказа в истории заказов, переходим в ленту "
                        "заказов, проверяем наличие созданного ID заказа в ленте заказов")
    def test_check_orders_from_orders_in_history_in_orders_in_feed(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        order_id = main_page.create_order()
        main_page.click_profile_button()
        profile_page = ProfilePage(driver, URLS.MAIN_PAGE + URLS.PROFILE_PAGE)
        profile_page.click_orders_history_link()
        feed_page = FeedPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.check_order_id_in_history_id(order_id)
        main_page.click_orders_feed_button()
        feed_page.check_order_id_in_feed(order_id)

    @allure.title("Проверка увеличения счетчика 'Выполнено за всё время' после создания заказа")
    @allure.description("Логин в систему, открываем страницу 'Лента заказов', сохраняем значение счетчика заказов за "
                        "всё время, переходим в конструктор, создаем заказ, открываем страницу 'Лента заказов', "
                        "сравниваем значение счетчика с предыдущим")
    def test_feed_page_increase_all_time_counter(self, driver, login_user):
        feed_page = FeedPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.open_page()
        counter_before = feed_page.check_number_or_all_time_orders()
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_constructor_button()
        main_page.create_order()
        feed_page.open_page()
        counter_after = feed_page.check_number_or_all_time_orders()
        feed_page.check_counter_increase(counter_before, counter_after)

    @allure.title("Проверка увеличения счетчика 'Выполнено за сегодня' после создания заказа")
    @allure.description("Логин в систему, открываем страницу 'Лента заказов', сохраняем значение счетчика заказов за "
                        "сегодня, переходим в конструктор, создаем заказ, открываем страницу 'Лента заказов', "
                        "сравниваем значение счетчика с предыдущим")
    def test_feed_page_increase_today_counter(self, driver, login_user):
        feed_page = FeedPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.open_page()
        counter_before = feed_page.check_number_of_today_counter()
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.create_order()
        feed_page.open_page()
        counter_after = feed_page.check_number_of_today_counter()
        feed_page.check_counter_increase(counter_before, counter_after)

    @allure.title("Проверка наличия заказа в разделе 'В работе' после создания заказа")
    @allure.description("Логин в систему, создаем заказ, переходим на страницу ленты заказов, проверяем наличие ID "
                        "созданного заказа в разделе 'В работе'")
    def test_feed_page_orders_in_work(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        order_id = main_page.create_order()
        feed_page = FeedPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.open_page()
        feed_page.check_order_id_in_list_of_orders_in_work(order_id)
