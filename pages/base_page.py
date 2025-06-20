import allure

from re import Pattern
from playwright.sync_api import Page, expect


class BasePage:
    """
    Базовый класс для всех Page Objects
    """
    def __init__(self, page: Page):
        self.page = page

    def  visit(self, url: str):
        """
        Метод открывает указанную страницу по URL и ожидает завершения загрузки сети.

        :param url: Адрес страницы, на которую нужно перейти.
        """
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        """
        Метод перезагружает текущую страницу и ожидает завершения загрузки сети.
        """
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        """
        Метод для проверки текущего URL
        :param expected_url: Ожидаемый url
        """
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
