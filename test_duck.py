from selene import browser, be, have
import pytest


@pytest.fixture
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://duckduckgo.com/')

    yield browser
    browser.quit()


def test_selene(setup_browser):
    setup_browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()

    setup_browser.element('[data-testid="web-vertical"]').should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))
