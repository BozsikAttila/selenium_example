class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def goto(self):
        self.driver.get(self.url)

