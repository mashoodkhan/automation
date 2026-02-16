from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    username_input = (By.ID,'username')
    password_input = (By.ID,'password')
    login_btn      = (By.XPATH,"//button/i[contains(text(),' Login')]")
    success_msg    = (By.CSS_SELECTOR,"div[class='flash success']")

    def login_to_site(self,url):
        self.load_url(url)
        self.set_text(self.username_input,"tomsmith")
        self.set_text(self.password_input,"SuperSecretPassword!")
        self.click(self.login_btn)
        self.wait_for_element_visible(self.success_msg)

    def get_login_success_msg(self):
        return self.get_text(self.success_msg)
