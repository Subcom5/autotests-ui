from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    """
    Класс описывает взаимодействие с компонентом - панель управления курсом
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self, is_create_course_disabled: bool = True):
        """
        Метод проверяет корректное отображение элементов в зависимости от полноты заполнения формы курса и
        наличия загруженного изображения

        :param is_create_course_disabled: флаг видимости кнопки создания курса
        """
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Create course')

        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()

        if not is_create_course_disabled:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        """
        Метод имитирует нажатие кнопки создания курса, если она активна
        """
        expect(self.create_course_button).to_be_enabled()
        self.create_course_button.click()
