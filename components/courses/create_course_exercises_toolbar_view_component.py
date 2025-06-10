import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    """
    Класс описывает взаимодействие с компонентом - панель управления упражнением
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_exercise_button = Button(
            page,'create-course-exercises-box-toolbar-create-exercise-button', 'Create exercise'
        )

    @allure.step('Checking the visibility of the exercises list toolbar')
    def check_visible(self):
        """
        Метод проверяет корректное отображение элементов панели управления упражнением
        :return:
        """
        self.title.check_visible()
        self.title.check_have_text('Exercises')

        self.create_exercise_button.check_visible()

    @allure.step('Click the create exercise button')
    def click_create_exercise_button(self):
        """
        Метод имитирует нажатие кнопки создания упражнения
        """
        self.create_exercise_button.check_visible()
        self.create_exercise_button.click()
