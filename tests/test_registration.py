from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    login_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    login_input.fill('password')

    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()
    registration_button.click()

    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
