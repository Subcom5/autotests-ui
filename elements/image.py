from elements.base_element import BaseElement


class Image(BaseElement):
    """
    Класс реализует компонент - image
    """
    @property
    def type_of(self) -> str:
        return "image"
