from playwright.sync_api import Page, Locator, expect


class BaseElement:
    """
    Базовый класс от которого будут наследоваться все остальные элементы
    """
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, **kwargs) -> Locator:
        """
        Метод позволяет динамически получить локатор для элемента на странице
        """
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    def click(self, **kwargs):
        """
        Метод для нажатия на элемент
        """
        locator = self.get_locator(**kwargs)
        locator.click()

    def check_visible(self, **kwargs):
        """
        Метод для проверки видимости элемента на странице
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        """
        Метод для проверки наличия конкретного текста в элементе
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
