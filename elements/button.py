from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    """
    Класс реализует компонент - button
    """
    def check_enabled(self, nth: int = 0, **kwargs):
        """
        Метод проверяет, что кнопка активна
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        """
        Метод проверяет, что кнопка не активна
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled()
