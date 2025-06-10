import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    """
    Класс для взаимодействия с компонентами navbar
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'App title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome title')

    @allure.step("Check visible title navbar")
    def check_visible(self, username: str):
        """
        Метод проверки видимости и содержания заголовков navbar

        :param username: Имя пользователя
        """
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
