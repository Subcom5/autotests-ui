from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        login_input = page.get_by_test_id('registration-form-password-input').locator('input')
        login_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_visible()
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        toolbar_title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(toolbar_title_courses).to_be_visible()
        expect(toolbar_title_courses).to_have_text('Courses')

        icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon).to_be_visible()

        view_title_course = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(view_title_course).to_be_visible()
        expect(view_title_course).to_have_text('There is no results')

        view_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(view_description).to_be_visible()
        expect(view_description).to_have_text('Results from the load test pipeline will be displayed here')
