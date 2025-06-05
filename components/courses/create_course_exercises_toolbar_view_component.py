from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    """
    Класс описывает взаимодействие с компонентом - панель управления упражнением
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def check_visible(self):
        """
        Метод проверяет корректное отображение элементов панели управления упражнением
        :return:
        """
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Exercises')

        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        """
        Метод имитирует нажатие кнопки создания упражнения
        """
        expect(self.create_exercise_button).to_be_visible()
        self.create_exercise_button.click()
