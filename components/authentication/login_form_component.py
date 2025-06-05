from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    """
    Класс описывает взаимодействие с компонентом - форма входа
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

    def fill(self, email: str, password: str):
        """
        Метод заполняет данными форму входа

        :param email: Почта
        :param password: Пароль
        """
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def check_visible(self, email: str, password: str):
        """
        Метод проверяет корректность отображения формы входа и валидность данных

        :param email: Почта
        :param password: Пароль
        """
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)
