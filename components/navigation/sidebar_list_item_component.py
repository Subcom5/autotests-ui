from typing import Pattern

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    """
    Класс реализует единый шаблон для компонентов боковой панели
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.icon = Icon(page,'{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, '{identifier}-drawer-list-item-title-text', 'Title')
        self.button = Button(page, '{identifier}-drawer-list-item-button', 'Button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str, identifier: str):
        """
        Метод проверяет видимость и содержание компонента боковой панели

        :param identifier: Идентификатор локатора
        :param title: Название компонента боковой панели
        """

        self.icon.check_visible(identifier=identifier)
        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)
        self.button.check_visible(identifier=identifier)

    def navigate(self, expected_url: Pattern[str], identifier: str):
        """
        Метод выполняет нажатие на компонент боковой панели, а затем проверяет,
        что выполнен переход на указанный url
        
        :param identifier: Идентификатор локатора
        :param expected_url: проверяемый url
        """

        self.button.click(identifier=identifier)
        self.check_current_url(expected_url)
