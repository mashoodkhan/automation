from dotenv import load_dotenv
import os
from pages.login_page import LoginPage

load_dotenv(verbose=True)

class Test_Logins:

    success_login = "You logged into a secure area!"

    def test_login(self,setup_webdriver):
        login_page = LoginPage(setup_webdriver)
        login_page.login_to_site(os.getenv("URL"))
        message = login_page.get_login_success_msg()
        assert self.success_login == message
