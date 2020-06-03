from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from resources.base_page import BasePage

class HomepageLocator(object):
    IMAGE = (By.XPATH, '//input[@accept="image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm"]')
    TWEET = (By.XPATH,'//div[@role="button"]//span[text()="Tweet"]')
    INPUT_TWEET = (By.XPATH, '//div[@role="textbox"]')
    SIDE_MENU = (By.XPATH, '//nav[@aria-label="Primary"][@role="navigation"]')
    LOADING_ANIMATION = (By.XPATH, '//div[starts-with(@aria-label, "Loading")]')
    IMAGE_UPLOADED = (By.XPATH, '//div[starts-with(@aria-label, "Image")]')
    PROFILE = (By.XPATH, '//div[@role="presentation"]')
    LOG_OUT = (By.XPATH, '//div[contains(text(),"Log out")]')
    LOG_OUT_POP_UP = (By.XPATH, '//div[@class="css-1dbjc4n r-1awozwy r-14lw9ot r-t23y2h r-1jgb5lz r-pm9dpa r-1ye8kvj r-1rnoaur r-d9fdf6 r-1sxzll1 r-13qz1uu"]')
    LOG_OUT_BUTTON_POP_UP = (By.XPATH, '//div[@role="button"]//span[text()="Log out"]')
    LOADING_PROGRESS = (By.XPATH, '//div[@role="progressbar"]')
    SETTING_BUTTON = (By.XPATH, '//a[@aria-label="Settings"][@role="button"]')
    EXPLORE_IMAGE = (By.XPATH, '//div[starts-with(@aria-label, "Timeline: Explore")]')


class HomePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def upload_pict(self, picture_path):
        # WebDriverWait(self.driver, timeout=3).until(ec.visibility_of_all_elements_located(HomepageLocator.IMAGE))
        picture = self.driver.find_element(*HomepageLocator.IMAGE)
        picture.send_keys(picture_path)

    def input_tweet(self, text_tweet):
        super().type_to_field(HomepageLocator.INPUT_TWEET, text_tweet)

    def click_tweet(self):
        super().click_button(HomepageLocator.TWEET)

    def homepage_must_be_displayed(self):
        super().wait_for_loading(HomepageLocator.LOADING_ANIMATION)
        WebDriverWait(self.driver, timeout=3).until(ec.visibility_of_all_elements_located(HomepageLocator.SIDE_MENU))

    def image_must_be_displayed(self):
        super().wait_until_visible(HomepageLocator.IMAGE_UPLOADED)

    def click_profile(self):
        super().click_button(HomepageLocator.PROFILE)

    def click_logout(self):
        super().click_button(HomepageLocator.LOG_OUT)

    def wait_logout_popup(self):
        super().wait_until_visible(HomepageLocator.LOG_OUT_POP_UP)

    def click_logout_in_popup(self):
        super().click_button(HomepageLocator.LOG_OUT_BUTTON_POP_UP)

    def logout_must_displayed(self):
        super().wait_for_loading(HomepageLocator.LOADING_PROGRESS)
        WebDriverWait(self.driver, timeout=5).until(ec.visibility_of_all_elements_located(HomepageLocator.EXPLORE_IMAGE))

