from elements.base_element import BaseElement


class Text(BaseElement):
    """
    Класс реализует компонент - text
    """
    @property
    def type_of(self) -> str:
        return "text"
