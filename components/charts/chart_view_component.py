from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


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

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self, title: str):
        """
        Метод проверяет корректное отображение элементов компонента

        :param title: Название компонента ['Students', 'Activities', 'Courses', 'Scores']
        """
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.chart).to_be_visible()
