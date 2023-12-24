import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators


class ProfilePage(BasePage):
    @allure.step("Нажать на ссылку 'История заказов'")
    def click_orders_history_link(self):
        self.find_element_and_click(ProfilePageLocators.ORDERS_HISTORY_LINK)

    @allure.step("Нажать на ссылку 'Выход'")
    def click_exit_profile_link(self):
        self.find_element_and_click(ProfilePageLocators.EXIT_BUTTON)

    @allure.step("Проверка выхода из профиля - наличие кнопки 'Войти'")
    def check_login_button_after_exit_from_profile(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_BUTTON), ("Выход из профиля не осуществлен, кнопка "
                                                                         "'Войти' отсутствует")

    @allure.step("Проверка перехода на страницу профиля - наличие кнопки 'Сохранить'")
    def check_save_button_on_profile_page(self):
        assert self.is_element_displayed_on_page(ProfilePageLocators.SAVE_BUTTON), ("Кнопка 'Сохранить' на станице "
                                                                                    "профиля не найдена")

    @allure.step("Проверка перехода на страницу истории заказов - ссылка активная")
    def check_history_button_is_active(self):
        history_link = self.find_element(ProfilePageLocators.ORDERS_HISTORY_LINK)
        assert 'link_active' in history_link.get_attribute('class'), ("Переход на страницу 'История заказов' не "
                                                                      "осуществлен, ссылка 'История заказов'"
                                                                      "не активна")
