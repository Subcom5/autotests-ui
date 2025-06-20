import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    """
    Класс описывает компонент - форма отсутствия курса или упражнения
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.icon = Icon(page, '{identifier}-empty-view-icon', 'Icon')
        self.title = Text(page, '{identifier}-empty-view-title-text', 'Title')
        self.description = Text(page, '{identifier}-empty-view-description-text', 'Description')

    @allure.step('Check visible empty view "{title}"')
    def check_visible(self, title: str, description: str, identifier: str):
        """
        Метод проверяет наличие иконки, наличие и корректность основной надписи и надписи пояснения формы

        :param identifier: Идентификатор локатора
        :param title: Основная надпись
        :param description: Пояснение
        """

        self.icon.check_visible(identifier=identifier)
        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)
        self.description.check_visible(identifier=identifier)
        self.description.check_have_text(description, identifier=identifier)
