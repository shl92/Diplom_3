import allure
from pages.base_page import BasePage
from locators.restore_page_locators import RestorePageLocators
from helpers import ProfileMethods


class RestorePage(BasePage):
    @allure.step("Нажать на ссылку 'Восстановление пароля'")
    def open_recovery_page(self):
        self.find_element_and_click(RestorePageLocators.RECOVER_PASSWORD_LINK)

    @allure.step("Заполнить поле 'email'")
    def input_email(self):
        self.find_element_and_send_text(RestorePageLocators.EMAIL_FIELD, ProfileMethods.generate_user()['email'])

    @allure.step("Нажать на кнопку 'Восстановить'")
    def click_recover_button(self):
        self.find_element_and_click(RestorePageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step("Нажать на кнопку 'Показать/скрыть пароль'")
    def click_show_password(self):
        self.find_element_and_click(RestorePageLocators.SHOW_HIDE_BUTTON)

    @allure.step("Проверка, что поле пароля активное")
    def check_active_field(self):
        password_field = self.find_element(RestorePageLocators.PASSWORD_FIELD)
        assert 'active' in password_field.get_attribute('class'), f"Поле 'Пароль' не активно"

    @allure.step("Проверка перехода на страницу восстановления пароля -  наличие поля 'email' на странице")
    def check_email_field_on_recovery_page(self):
        assert self.is_element_displayed_on_page(RestorePageLocators.EMAIL_FIELD), (f"Поле email на странице "
                                                                                    f"восстановления пароля не "
                                                                                    f"найдено.")

    @allure.step("Проверка перехода по кнопке 'Восстановить' - наличие поля 'Пароль' на странице")
    def check_password_field_after_recovery_button(self):
        assert self.is_element_displayed_on_page(RestorePageLocators.PASSWORD_FIELD), ("Поле 'Пароль' на странице "
                                                                                       "восстановления пароля не "
                                                                                       "найдено.")
