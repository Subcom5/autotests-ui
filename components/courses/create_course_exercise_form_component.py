from playwright.sync_api import expect

from components.base_component import BaseComponent


class CreateCourseExerciseFormComponent(BaseComponent):
    """
    Класс для работы с формой для создания и редактирования упражнений
    """
    def click_delete_button(self, index: int):
        """
        Метод удаления упражнения по его индексу

        :param index: Индекс упражнения
        """
        delete_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_button.click()

    def check_visible(self, index: int, title: str, description: str):
        """
        Метод проверки формы упражнения по индексу

        :param index: Индекс упражнения
        :param title: Название упражнения
        :param description: Описание упражнения
        """
        subtitle = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-subtitle-text")
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

    def fill(self, index: int, title: str, description: str):
        """
        Метод для заполнения формы создания упражнения

        :param index: Индекс упражнения
        :param title: Название упражнения
        :param description: Описание упражнения
        """
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)
