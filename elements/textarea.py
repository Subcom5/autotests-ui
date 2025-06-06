from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Textarea(BaseElement):
    """
    Класс реализует компонент - textarea
    """
    def get_locator(self, **kwargs) -> Locator:
        """
        Метод(переопределенный) позволяет динамически получить локатор для элемента textarea
        """
        return super().get_locator(**kwargs).locator('textarea').first

    def fill(self, value: str, **kwargs):
        """
        Метод заполняет данными элемент textarea
        """
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        """
        Метод проверяет введенные данные в элемент textarea
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
