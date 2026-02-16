from selenium.common import TimeoutException, ElementNotVisibleException
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver,10)
        self.driver = driver

    def load_url(self,locator):
        self.driver.get(locator)
        return self.driver.title

    def wait_for_element_visible(self,locator):
        try:
            self.wait.until(
            EC.visibility_of_element_located(locator))
        except TimeoutException | ElementNotVisibleException as e:
            print(e)

    def is_element_visible(self, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click(self,locator):
        self.wait_for_element_visible(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def set_text(self,locator,value):
        self.wait_for_element_visible(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def select_option_by_value(self,locator,value):
        x = self.driver.Select(locator).select_by_value(value)
        return x.first_selected_option