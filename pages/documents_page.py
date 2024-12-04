import time

from playwright.sync_api import expect
from selenium.webdriver import Keys


class documentsPage():

    def __init__(self, page):
        self.__page = page
        self.page = page
        self.__guides_button = self.__page.get_by_text("Cloud Guides")
        self.__document_buttons_locator = "a[class='fp-docs-banner-btn']"




    def get_release_note_version(self):
        expect(self.__guides_button).to_be_visible()

        buttons = self.__page.query_selector_all(self.__document_buttons_locator)
        button_text= buttons[1].text_content()
        before_index = button_text.index(" ")
        after_index = button_text.index("Rel")
        release_from_button = button_text[before_index:after_index].strip()
        return release_from_button



    def get_referance_manual_version(self):
        expect(self.__guides_button).to_be_visible()

        buttons = self.__page.query_selector_all(self.__document_buttons_locator)
        button_text = buttons[0].text_content()
        before_index = button_text.index(" ")
        after_index = button_text.index("Ref")
        release_from_button  = button_text[before_index:after_index].strip()
        return release_from_button





