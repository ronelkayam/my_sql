import time

from playwright.sync_api import expect
from selenium.webdriver import Keys


class welcomePage():

    def __init__(self, page):
        self.__page = page
        self.page = page
        self.__logout_link = self.__page.get_by_text("logout")




    def is_welcome_page_appears(self):
        try:
            expect(self.__logout_link).to_be_visible()
            return self.__logout_link.is_visible()
        except Exception as e:
            print("log out button did not found probably login fail")
            return False

    def navigate_to_documents(self):
        buttons = self.__page.query_selector_all("a[href='https://dev.mysql.com/doc/']")
        buttons[0].click()






