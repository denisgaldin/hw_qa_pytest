from selene import browser, be, have


def test_duckduckgo_search():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element("[data-testid=web-vertical]").should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))
