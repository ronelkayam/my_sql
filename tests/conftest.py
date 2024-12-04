import time

import pytest


from playwright.sync_api import sync_playwright

from my_sql.commons.globals import URL, BROWSER
from my_sql.pages.documents_page import documentsPage
from my_sql.pages.login_page import loginPage
from my_sql.pages.register_page import registerPage
from my_sql.pages.welcome_page import welcomePage


@pytest.fixture()
def setup_browser():
    with sync_playwright() as playwright:
        if (BROWSER == 1):
            browser = playwright.chromium.launch(headless=False)
        else:
            browser = playwright.firefox.launch(headless=False)

        page = browser.new_page()
        page.goto(URL)
        login_page = loginPage(page)
        register_page = registerPage(page)
        welcome_page = welcomePage(page)
        doc_page = documentsPage(page)

        yield page , login_page, register_page,welcome_page,doc_page
        page.close()
        browser.close()
        print("Test end")

