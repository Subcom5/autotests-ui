from playwright.sync_api import Page, Locator, expect


class BaseElement:
    """
    Базовый класс от которого будут наследоваться все остальные элементы
    """
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Метод позволяет динамически получить локатор для элемента на странице

        :return: Возвращает динамически сформированный локатор, с указанным индексом
        """
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        """
        Метод для нажатия на элемент
        """
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        """
        Метод для проверки видимости элемента на странице
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        """
        Метод для проверки наличия конкретного текста в элементе
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
