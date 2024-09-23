import pytest
from selene import browser, be, have


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://duckduckgo.com'
    browser.config.timeout = 10
    yield
    browser.quit()


def test_duckduckgo_search():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element("[data-testid=web-vertical]").should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))
