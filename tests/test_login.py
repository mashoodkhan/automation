import pytest
from dotenv import load_dotenv
import os
from pages.login_page import LoginPage

load_dotenv(verbose=True)

class Test_Logins:

    success_login = "You logged into a secure area!"

    @pytest.mark.smoke
    def test_login(self,setup_webdriver):
        login_page = LoginPage(setup_webdriver)
        login_page.login_to_site(os.getenv("TARGET_URL")+"/login")
        print("OPENED URL ", os.getenv("TARGET_URL")+"/login")
        message = login_page.get_login_success_msg()
        assert self.success_login in message
        print("LOGGED IN SUCCESSFULLY")

    @pytest.mark.regression
    def test_regression(self, setup_webdriver):
        pass
