from playwright.sync_api import expect


class loginPage():

    def __init__(self, page):
        self.__page = page
        self.page = page
        self.__user = self.__page.locator("[id='idcs-signin-basic-signin-form-username']")
        self.__login = self.__page.get_by_text("Login")
        self.__next = self.__page.get_by_text("Next")
        self.__password = self.__page.locator("[id='idcs-auth-pwd-input|input']")
        self.__sign_in = self.__page.get_by_text("Sign In")



    def login_by_user_password(self, user_text,password_text):
        print(f"try to login with user {user_text}")
        self.__login.click()
        expect(self.__user).to_be_visible()

        self.__user.click()
        self.__user.fill(user_text)
        self.__next.click()
        expect(self.__password).to_be_visible()

        self.__password.click()
        self.__password.fill(password_text)
        self.__page.keyboard.press('Enter')




