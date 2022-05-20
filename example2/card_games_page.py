from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import BasePage
from base_element import BaseElement
from locator import Locator


class CardGamesPage(BasePage):

    url = "https://www.metagames.hu/gyujtogetos-kartyajatekok"

    @property
    def magic_cards_link(self):
        locator = Locator(by=By.XPATH, value="//h2[text() = 'Magic: the Gathering']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def first_element_add_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.justify-content-start > div:first-child .btn-primary')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def first_element_name(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.justify-content-start > div:first-child .webshop-list-item-name')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def sort_by_price(self):
        Select(self.driver.find_element(By.XPATH, '//*[@id="sortForm"]/select[1]')).select_by_index(4)
        return None
