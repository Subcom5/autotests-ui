from playwright.sync_api import Page


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
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        """
        Метод перезагружает текущую страницу и ожидает завершения загрузки сети.
        """
        self.page.reload(wait_until='networkidle')
