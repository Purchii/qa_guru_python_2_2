import pytest
from selene import browser, be, have
import conftest





def test_google_should_find_selene(open_browser_set_reso):
    browser.element('[name="q"]').should(be.blank).type('selene git').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
