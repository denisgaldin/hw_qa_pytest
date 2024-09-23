from selene import browser, be, have
import pytest


@pytest.fixture
def setup_browser():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    return browser


def test_selene(setup_browser):
    assert setup_browser.element('[data-testid=web-vertical]').should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))
