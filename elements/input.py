from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):
    """
    Класс реализует компонент - input
    """
    def get_locator(self, **kwargs) -> Locator:
        """
        Метод(переопределенный) позволяет динамически получить локатор для элемента input
        """
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value: str, **kwargs):
        """
        Метод заполняет данными элемент input
        """
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        """
        Метод проверяет введенные данные в элемент input
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
