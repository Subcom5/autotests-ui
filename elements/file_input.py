import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    """
    Класс реализует компонент - file_input
    """
    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        """
        Метод передает путь к файлу
        """
        with allure.step(f'Set file "{file}" to the {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
