from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    print("open the browser")


def test_first(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - Woikipedia'))
    print(open_browser)