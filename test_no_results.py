from selene import be, have


def test_no_results(setup_browser):
    setup_browser.element('[name="q"]').should(be.blank).type('sdfajsdfadkjf').press_enter()
    setup_browser.element('[data-testid=web-vertical]').should(
        have.text('По запросу sdfajsdfadkjf результаты не найдены.'))
