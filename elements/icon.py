from elements.base_element import BaseElement


class Icon(BaseElement):
    """
    Класс реализует компонент - icon
    """
    @property
    def type_of(self) -> str:
        return "icon"
