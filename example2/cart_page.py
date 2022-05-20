from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from locator import Locator


class CartPage(BasePage):
    url = 'https://www.metagames.hu/kosar'

    @property
    def name_of_item(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.cart-item div a')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def number_of_item(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.cart-item input')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
