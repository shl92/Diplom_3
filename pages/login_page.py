import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):
    @allure.step("Заполнить поле 'email'")
    def input_email(self, login):
        self.find_element_and_send_text(LoginPageLocators.EMAIL_INPUT, login)

    @allure.step("Заполнить поле 'пароль'")
    def input_password(self, password):
        self.find_element_and_send_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать на кнопку 'Войти'")
    def login_button_click(self):
        self.find_element_and_click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Проверка логина в систему - наличие кнопки 'Оформить заказ'")
    def check_login(self):
        assert self.is_element_present(MainPageLocators.CREATE_ORDER_BUTTON), 'Логин в систему не осуществлен'

    @allure.step("Осуществить логин в систему")
    def login(self, login, password):
        self.input_email(login)
        self.input_password(password)
        self.login_button_click()
        self.check_login()
