import time

from playwright.sync_api import expect


class registerPage():

    def __init__(self, page):
        self.__page = page
        self.__email_menu = self.__page.locator("[id='sView1:r1:0:email::content']")
        self.__password_menu = self.__page.locator("[id='sView1:r1:0:password::content']")
        self.__retype_password_menu = self.__page.locator("[id='sView1:r1:0:retypePassword::content']")
        self.__first_name_menu = self.__page.locator("[id='sView1:r1:0:firstName::content']")
        self.__last_name_menu = self.__page.locator("[id='sView1:r1:0:lastName::content']")
        self.__job_menu = self.__page.locator("[id='sView1:r1:0:jobTitle::content']")
        self.__phone_menu = self.__page.locator("[id='sView1:r1:0:workPhone::content']")
        self.__company_menu = self.__page.locator("[id='sView1:r1:0:companyName::content']")
        self.__address_menu = self.__page.locator("[id='sView1:r1:0:address1::content']")
        self.__city_menu = self.__page.locator("[id='sView1:r1:0:city::content']")
        self.__zip_menu = self.__page.locator("[id='sView1:r1:0:postalCode::content']")
        self.__register = self.__page.get_by_text("Register")
        self.__create_account = self.__page.get_by_text("Create Account")


    def click_and_fill_menu(self, element, text):
        expect(element).to_be_visible()
        element.click()
        element.clear()
        element.fill(text)

    def click_on_register_if_exist(self):
        print(f"Try to navigate to register page ")
        if (self.__register.is_visible()):
            self.__register.click()


    def create_new_user(self,user_details):
        self.click_and_fill_menu(self.__email_menu,user_details["email"])
        self.click_and_fill_menu(self.__password_menu,user_details["password"])
        time.sleep(3) # adding fix delay due stability issues
        self.click_and_fill_menu(self.__retype_password_menu,user_details["password"])
        self.click_and_fill_menu(self.__first_name_menu,user_details["first_name"])
        self.click_and_fill_menu(self.__last_name_menu,user_details["last_name"])
        self.click_and_fill_menu(self.__job_menu,user_details["job"])
        self.click_and_fill_menu(self.__phone_menu,user_details["phone"])
        self.click_and_fill_menu(self.__company_menu,user_details["company_name"])
        self.click_and_fill_menu(self.__address_menu,user_details["address"])
        self.click_and_fill_menu(self.__city_menu,user_details["city"])
        self.click_and_fill_menu(self.__zip_menu,user_details["zip"])
        # the test did not actually create account
        #self.__create_account.click()











