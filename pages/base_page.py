from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://ya.ru/'

    def find(self, locator, value):
        return self.browser.find_element(locator, value)

    def find_element_wait(self, locator, value):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((locator, value)))

    def open(self):
        self.browser.get(self.url)
