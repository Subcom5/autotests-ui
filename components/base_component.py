from playwright.sync_api import Page, expect
from typing_extensions import Pattern


class BaseComponent:
    """
    Базовый класс для всех page components
    """
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        """
         Метод проверяет, что текущий URL страницы соответствует регулярному выражению expected_url

        :param expected_url: Регулярное выражение
        """
        expect(self.page).to_have_url(expected_url)
