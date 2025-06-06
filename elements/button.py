from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    """
    Класс реализует компонент - button
    """
    def check_enabled(self, **kwargs):
        """
        Метод проверяет, что кнопка активна
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs):
        """
        Метод проверяет, что кнопка не активна
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()
