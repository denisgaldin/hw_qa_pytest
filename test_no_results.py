import pytest
from selene import browser, element, be, have, by


def test_no_results(setup_browser):
    setup_browser.element('[name="q"]').should(be.blank).type('sdfajsdfadkjf').press_enter()
    setup_browser.element('.no-results').should(have.text('По запросу sdfajsdfadkjf результаты не найдены.'))
