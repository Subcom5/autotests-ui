import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    """
    Класс описывает взаимодействие с компонентом - диаграмма
    """
    def __init__(self, page: Page, identifier: str, chart_type: str):
        """
        шаблон - {'identifier': chart_type}
        [{'students':'bar'}, {'activities':'line'}, {'scores':'scatter'}, {'courses':'pie'}]
        """
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible chart view at title "{title}"')
    def check_visible(self, title: str):
        """
        Метод проверяет корректное отображение элементов компонента

        :param title: Название компонента ['Students', 'Activities', 'Courses', 'Scores']
        """
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()
