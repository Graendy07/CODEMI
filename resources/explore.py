from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from resources.base_page import BasePage

class ExploreLocator(object):
    USERNAME = (By.NAME, "session[username_or_email]")
    PASSWORD = (By.NAME, "session[password]")
    LOGIN_BTN = (By.XPATH, '//div[@role="button"]//span[text()="Log in"]')


class ExplorePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def open_twitter(self):
        self.driver.get('https://twitter.com/')

    def login(self, username, password):
        super().type_to_field(ExploreLocator.USERNAME, username)
        super().type_to_field(ExploreLocator.PASSWORD, password)
        super().click_button(ExploreLocator.LOGIN_BTN)