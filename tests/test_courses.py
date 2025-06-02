from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    toolbar_title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(toolbar_title_courses).to_be_visible()
    expect(toolbar_title_courses).to_have_text('Courses')

    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    view_title_course = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(view_title_course).to_be_visible()
    expect(view_title_course).to_have_text('There is no results')

    view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(view_description).to_be_visible()
    expect(view_description).to_have_text('Results from the load test pipeline will be displayed here')
