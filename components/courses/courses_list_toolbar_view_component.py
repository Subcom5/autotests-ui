import re
import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesListToolbarViewComponent(BaseComponent):
    """
    Класс описывает работу с компонентом - панель инструментов списка курсов

    Компонент CoursesListToolbarView состоит из двух элементов:
    title — заголовок "Courses"
    create_course_button — кнопка создания курса
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'Title')
        self.create_course_button = Button(
            page, 'courses-list-toolbar-create-course-button', 'Create course'
        )
    @allure.step('Checking the visibility of the courses list toolbar')
    def check_visible(self):
        """
        Метод проверяет отображение элементов и корректное название заголовка "Courses "
        """
        self.title.check_visible()
        self.title.check_have_text('Courses')

        self.create_course_button.check_visible()

    @allure.step('Click the create course button')
    def click_create_course_button(self):
        """
        Метод имитирует нажатие на кнопку создания курса и проверяет, что выполнился редирект на нужный url
        """
        self.create_course_button.click()
        self.check_current_url(re.compile(".*/#/courses/create"))
