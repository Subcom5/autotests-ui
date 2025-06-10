import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    """
    Класс описывает взаимодействие с компонентом - панель управления дашбордом
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Title')

    @allure.step("Check visible title dashboard toolbar")
    def check_visible(self):
        """
        Метод проверяет отображение и корректное название заголовка "Dashboard"
        """
        self.title.check_visible()
        self.title.check_have_text('Dashboard')
