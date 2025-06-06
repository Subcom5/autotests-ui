from elements.base_element import BaseElement


class FileInput(BaseElement):
    """
    Класс реализует компонент - file_input
    """
    def set_input_files(self, file: str, **kwargs):
        """
        Метод передает путь к файлу
        """
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)
