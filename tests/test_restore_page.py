import allure
from pages.restore_page import RestorePage
from data.urls import URLS


@allure.feature("Проверка функционала на странице восстановления пароля")
class TestRestorePage:
    @allure.title("Проверка перехода на страницу восстановления пароля по ссылке 'Восстановить пароль'")
    @allure.description("Открываем страницу входа (логина), нажимаем на ссылку 'Восстановить пароль', проверяем "
                        "наличие поля 'email' на странице восстановления пароля")
    def test_restore_password_link_click(self, driver):
        login_page = RestorePage(driver, URLS.LOGIN_PAGE)
        login_page.open_page()
        restore_page = RestorePage(driver, URLS.RESTORE_PAGE)
        restore_page.open_recovery_page()
        restore_page.check_email_field_on_recovery_page()

    @allure.title("Проверка ввода почты и клика по кнопке 'Восстановить'")
    @allure.description("Открываем страницу восстановления пароля, вводим email, нажимам на кнопку 'Восстановить', "
                        "проверяем наличие поля 'Пароль' на странице восстановления пароля")
    def test_input_email_and_restore_button_click(self, driver):
        restore_page = RestorePage(driver, URLS.RESTORE_PAGE)
        restore_page.open_page()
        restore_page.input_email()
        restore_page.click_recover_button()
        restore_page.check_password_field_after_recovery_button()

    @allure.title("Проверка подсветки поля пароля после клика на кнопку 'показать/скрыть пароль'")
    @allure.description("Открываем страницу восстановления пароля, вводим email, нажимам на кнопку 'Восстановить', "
                        "нажимаем на кнопку 'показать/скрыть пароль', проверяем, что поле стало активно (подсвечено)")
    def test_show_restore_password_click_field_active(self, driver):
        restore_page = RestorePage(driver, URLS.RESTORE_PAGE)
        restore_page.open_page()
        restore_page.input_email()
        restore_page.click_recover_button()
        restore_page.click_show_password()
        restore_page.check_active_field()
