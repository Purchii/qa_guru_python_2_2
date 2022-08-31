import pytest
from selene import browser

@pytest.fixture()
def open_browser_set_reso():

    browser.open('https://google.com/ncr')
    browser.driver().set_window_size(1440,900)