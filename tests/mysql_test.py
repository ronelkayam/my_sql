
import pytest

from my_sql.commons.globals import USER_DETAILS, EXIST_USER, EXIST_PASSWORD, REF_MANUAL_VERSION, RELEASE_NOTE_VERSION


class TestMysql():
    def test_create_user(self, setup_browser):
        page, login_page, register_page,welcome_page = setup_browser

        register_page.click_on_register_if_exist()
        register_page.create_new_user(USER_DETAILS)
        login_page.login_by_user_password(USER_DETAILS["email"], USER_DETAILS["password"])
        is_success = welcome_page.is_welcome_page_appears()
        assert is_success == True ,"login with new user after succeed to created did not success as expected "


    def test_login_with_exist_user(self, setup_browser):
        page, login_page, register_page,welcome_page = setup_browser

        login_page.login_by_user_password(EXIST_USER,EXIST_PASSWORD)
        is_success = welcome_page.is_welcome_page_appears()
        assert is_success == True , "login with exist user did not success as expected "

    def test_login_with_none_exist_user(self, setup_browser):
        page, login_page, register_page, welcome_page = setup_browser

        login_page.login_by_user_password("abc@walla.co.il", "12345")
        is_success = welcome_page.is_welcome_page_appears()
        assert is_success == False, "login with none exist user success not as expected "

    def test_login_with_exist_user_incorrect_password(self, setup_browser):
        page, login_page, register_page, welcome_page = setup_browser

        login_page.login_by_user_password(EXIST_USER, "12345")
        is_success = welcome_page.is_welcome_page_appears()
        assert is_success == False, "login with  exist and incorrect password success not as expected"

    def test_getting_referance_manual_version(self,setup_browser):
        page, login_page, register_page,welcome_page,doc_page = setup_browser
        login_page.login_by_user_password(EXIST_USER,EXIST_PASSWORD)
        welcome_page.is_welcome_page_appears()
        welcome_page.navigate_to_documents()
        ref_release = doc_page.get_referance_manual_version()
        assert ref_release == REF_MANUAL_VERSION, "Reference manual version is not as expected"

    def test_getting_release_notes_version(self,setup_browser):
        page, login_page, register_page,welcome_page,doc_page = setup_browser
        login_page.login_by_user_password(EXIST_USER,EXIST_PASSWORD)
        welcome_page.is_welcome_page_appears()
        welcome_page.navigate_to_documents()
        ref_release = doc_page.get_release_note_version()
        assert ref_release == RELEASE_NOTE_VERSION, "Release notes version is not as expected"




