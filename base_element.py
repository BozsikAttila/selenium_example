from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.find

    def find(self):
        self.web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    def text(self):
        text = self.web_element.text()
        return text




