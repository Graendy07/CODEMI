from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def type_to_field(self, field_locator, text):
        WebDriverWait(self.driver, timeout=3).until(ec.visibility_of_all_elements_located(field_locator))
        input_field = self.driver.find_element(*field_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(input_field)
        actions.click(input_field)
        actions.perform()
        input_field.clear()
        input_field.send_keys(text)

    def click_button(self, button_locator):
        WebDriverWait(self.driver, timeout=3).until(ec.visibility_of_all_elements_located(button_locator))
        button = self.driver.find_element(*button_locator)
        action = ActionChains(self.driver)
        action.move_to_element(button)
        action.click(button)
        action.perform()

    def wait_for_loading(self, loading_locator):
        WebDriverWait(self.driver, timeout=6).until(ec.invisibility_of_element_located(loading_locator))

    def wait_until_visible(self, item_locator):
        WebDriverWait(self.driver, timeout=6).until(ec.visibility_of_element_located(item_locator))

