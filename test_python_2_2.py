import pytest
from selene.support.shared import browser
from selene import be, have
import conftest





def test_google_should_find_selene(open_browser_set_reso):
    browser.element('[name="q"]').should(be.blank).type('selene git').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_google_should_find_selene_not(open_browser_set_reso):
    browser.element('[name="q"]').should(be.blank).type('djhgkjrhflkgdjhglfg;jld').press_enter()
    browser.element('[id="search"]').should(have.no.text('djhgkjrhflkgdjhglfg;jld'))
