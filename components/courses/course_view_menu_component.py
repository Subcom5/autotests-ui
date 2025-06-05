from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    """
    Класс описывает меню компонента - карточки курса
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

    def click_edit(self, index: int):
        """
        Метод открывает страницу редактирования курса через меню по индексу
        :param index: Индекс курса
        """
        self.menu_button.nth(index).click()

        expect(self.edit_menu_item.nth(index)).to_be_visible()
        self.edit_menu_item.nth(index).click()

    def click_delete(self, index: int):
        """
        Метод удаления курса по индексу
        :param index: Индекс курса
        """
        self.menu_button.nth(index).click()

        expect(self.delete_menu_item.nth(index)).to_be_visible()
        self.delete_menu_item.nth(index).click()
