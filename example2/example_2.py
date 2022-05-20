#Task: Navigate to the Magic the Gatering cars page in the webshop: Metagames.hu.
# Sort the page by price and add 2 of the most expensive items to the cart.

from selenium import webdriver

from card_games_page import CardGamesPage
from cart_page import CartPage

def example_2():
    #Configuratiion
    chrome_compatible_browser_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application/brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = chrome_compatible_browser_path

    browser = webdriver.Chrome(options=option)
    browser.maximize_window()

    #Setup

    card_games_page = CardGamesPage(browser)
    card_games_page.goto()

    #Test steps

    card_games_page.magic_cards_link.click()
    card_games_page.sort_by_price()
    card_games_page.first_element_add_button.click()
    card_games_page.first_element_add_button.click()

    #Validation - actual validatin can be to save the name of the most expensive
    # item and check the cart for the name and the number of items in it.

    cart_page = CartPage(browser)
    cart_page.goto()

    #Tear down
    input()
    browser.close()

if __name__ == '__main__':
    example_2()
