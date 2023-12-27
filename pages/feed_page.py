import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    @allure.step("Получить список заказов из истории заказов")
    def get_orders_id_list_from_history(self):
        self.is_element_present(FeedPageLocators.ORDER_ID_LIST)
        return self.find_elements(FeedPageLocators.ORDER_ID_LIST)

    @allure.step("Получить список заказов в работе")
    def get_list_of_orders_in_work(self):
        self.check_element_disappeared()
        return self.find_elements(FeedPageLocators.ORDERS_IN_WORK_LIST)

    @allure.step("Нажать на первый заказ в ленте заказов")
    def click_on_first_order_card(self):
        self.find_element_and_click(FeedPageLocators.NEWEST_ORDER_IN_FEED_LIST)

    @allure.step("Проверка наличия ID созданного заказа в истории заказов")
    def check_order_id_in_history_id(self, order_id):
        orders_list = self.get_orders_id_list_from_history()
        orders_from_list = [int(c.text[1:]) for c in orders_list]
        assert order_id in orders_from_list, f"Созданный заказ(ID: {order_id}) отсутствует в истории заказов"

    @allure.step("Проверка наличия ID созданного заказа в ленте заказов")
    def check_order_id_in_feed(self, order_id):
        orders_list = self.get_orders_id_list_from_history()
        orders_from_list = [int(c.text[1:]) for c in orders_list]
        assert order_id in orders_from_list, f"Созданный заказ (ID: {order_id}) отсутствует в ленте заказов"

    @allure.step("Проверка количества заказов за всё время")
    def check_number_or_all_time_orders(self):
        return int(self.find_element(FeedPageLocators.ORDER_COUNTER_ALL_TIME).text)

    @allure.step("Проверка количества заказов за сегодня")
    def check_number_of_today_counter(self):
        return int(self.find_element(FeedPageLocators.ORDER_COUNTER_TODAY).text)

    @allure.step("Проверка исчезновения элемента со страницы")
    def check_element_disappeared(self):
        self.find_element(FeedPageLocators.NO_ORDERS_IN_WORK)
        self.is_element_no_more_located(FeedPageLocators.NO_ORDERS_IN_WORK)

    @allure.step("Проверка наличия наличия ID созданного заказа в списке заказов в работе")
    def check_order_id_in_list_of_orders_in_work(self, order_id):
        orders_list = self.get_list_of_orders_in_work()
        orders_from_list = [int(c.text[1:]) for c in orders_list]
        assert order_id in orders_from_list, "Созданный заказ отсутствует в списке заказов в работе"

    @allure.step("Проверка открытия карточки заказа - наличие текста 'Состав'")
    def check_order_card_opened(self):
        assert self.find_element(FeedPageLocators.ORDER_CARD).text == 'Cостав', ("Карточка заказа не открылась, текст "
                                                                                 "'Состав' отсутствует")

    @allure.step("Проверка перехода на ленту заказов - наличие текста 'Лента заказов'")
    def check_text_order_feed_on_feed_page(self):
        assert self.is_element_displayed_on_page(FeedPageLocators.ORDER_FEED_TEXT), ("Текст 'Лента заказов' не найден "
                                                                                     "на странице ленты заказов")

    @allure.step("Проверка изменения счетчика заказов - до заказа и после заказа")
    def check_counter_increase(self, counter_before, counter_after):
        assert counter_before + 1 == counter_after, (f"Счетчик не увеличился на совершенный заказ. Значение до заказа:"
                                                     f" {counter_before}, значение после заказа: {counter_after}")
