import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    """
    Класс описывает взаимодействие с компонентом - панель управления курсом
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(
            page, 'create-course-toolbar-create-course-button', 'Create course'
        )

    @allure.step("Check visibility and state of form elements before course creation \
    (create button disabled: {is_create_course_disabled})")
    def check_visible(self, is_create_course_disabled: bool = True):
        """
        Метод проверяет корректное отображение элементов в зависимости от полноты заполнения формы курса и
        наличия загруженного изображения

        :param is_create_course_disabled: флаг видимости кнопки создания курса
        """
        self.title.check_visible()
        self.title.check_have_text('Create course')

        if is_create_course_disabled:
            self.create_course_button.check_disabled()

        if not is_create_course_disabled:
            self.create_course_button.check_enabled()

    @allure.step("Click the  create course button if enabled")
    def click_create_course_button(self):
        """
        Метод имитирует нажатие кнопки создания курса, если она активна
        """
        self.create_course_button.check_enabled()
        self.create_course_button.click()
