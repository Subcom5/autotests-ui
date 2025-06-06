from playwright.sync_api import Page

from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    """
    Page Object для страницы просмотра курсов
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.empty_view = EmptyViewComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)
        self.course_view = CourseViewComponent(page)

    def check_visible_empty_view(self):
        """
        Метод проверяет наличие и видимость иконки, заголовка и описания пустого блока
        """
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here',
            identifier='courses-list'
        )
