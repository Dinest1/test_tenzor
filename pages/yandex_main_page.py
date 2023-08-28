from pages.base_page import BasePage
from pages.locators import YandexSearchLocators


class YandexMainPage(BasePage):

    def search_box(self):
        return self.find(*YandexSearchLocators.SEARCH_BOX_LOCATOR)

    def enter_in_search_box(self, text='Тензор'):
        self.search_box().send_keys(text)

    def suggest_is_displayed(self):
        return self.find(*YandexSearchLocators.SUGGEST_LOCATOR)

    def click_on_button_submit(self):
        self.find(*YandexSearchLocators.BUTTON_SUBMIT_LOCATOR).click()

    def search_result(self):
        return self.find(*YandexSearchLocators.SEARCH_RESULT_LOCATOR)

    def search_link(self):
        return self.find(*YandexSearchLocators.SEARCH_LINK_LOCATOR).get_attribute('href')

