import allure
from pages.profle_page import ProfilePage
from data.urls import URLS
from pages.main_page import MainPage


@allure.feature("Проверка функционала на странице личного кабинета")
class TestProfilePage:
    @allure.title("Проверка перехода в личный кабинет по клику на кнопку 'Личный кабинет'")
    @allure.description("Логин в систему, открываем главную страницу сайта, нажимаем на кнопку 'Личный кабинет', "
                        "проверяем наличие кнопки 'Сохранить' на странице личного кабинета")
    def test_profile_button_click(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver, URLS.MAIN_PAGE + URLS.PROFILE_PAGE)
        profile_page.check_save_button_on_profile_page()

    @allure.title("Проверка перехода в раздел 'История заказов' по клику на ссылку 'История заказов'")
    @allure.description("Логин в систему, открываем страницу профиля, нажимаем на ссылку 'История заказов', "
                        "проверяем, что ссылка 'История заказов' активна (через атрибут класса ссылки)")
    def test_orders_history_link_click(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver, URLS.MAIN_PAGE + URLS.PROFILE_PAGE)
        profile_page.click_orders_history_link()
        profile_page.check_history_button_is_active()

    @allure.title("Проверка выхода из личного кабинета")
    @allure.description("Логин в систему, открываем страницу профиля, нажимаем на ссылку 'Выход', проверяем наличие "
                        "кнопки 'Войти'")
    def test_exit_profile(self, driver, login_user):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver, URLS.MAIN_PAGE + URLS.PROFILE_PAGE)
        profile_page.click_exit_profile_link()
        profile_page.check_login_button_after_exit_from_profile()
