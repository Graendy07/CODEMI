import unittest
from selenium import webdriver
from resources import explore
from resources import homepage

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        self.driver = driver
        ex = explore.ExplorePage(self.driver)
        ex.open_twitter()

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        ex = explore.ExplorePage(self.driver)
        home = homepage.HomePage(self.driver)
        ex.login('GraendyD', 'testing07')
        home.homepage_must_be_displayed()
        home.upload_pict('D:\CODEMI.jpg')
        home.input_tweet('CODEMI TEST')
        home.click_tweet()
        home.image_must_be_displayed()
        home.click_profile()
        home.click_logout()
        home.wait_logout_popup()
        home.click_logout_in_popup()
        home.logout_must_displayed()


