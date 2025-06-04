from typing import Pattern
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    """
    Класс реализует единый шаблон для компонентов боковой панели
    """
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')

    def check_visible(self, title: str):
        """
        Метод проверяет видимость и содержание компонента боковой панели

        :param title: Название компонента боковой панели
        """
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        """
        Метод выполняет нажатие на компонент боковой панели, а затем проверяет,
        что выполнен переход на указанный url
        
        :param expected_url:
        """
        self.button.click()
        self.check_current_url(expected_url)
