import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CoursesListToolbarViewComponent(BaseComponent):
    """
    Класс описывает работу с компонентом - панель инструментов списка курсов

    Компонент CoursesListToolbarView состоит из двух элементов:
    title — заголовок "Courses"
    create_course_button — кнопка создания курса
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible(self):
        """
        Метод проверяет отображение и корректное название заголовка "Courses"
        """
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Courses')

        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        """
        Метод имитирует нажатие на кнопку создания курса и проверяет, что выполнился редирект на нужный url
        """
        self.create_course_button.click()
        self.check_current_url(re.compile(".*/#/courses/create"))
