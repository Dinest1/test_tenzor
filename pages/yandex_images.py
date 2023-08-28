from pages.base_page import BasePage
from pages.locators import YandexImagesLocators


class YandexImages(BasePage):

    def search_box(self):
        return self.find_element_wait(*YandexImagesLocators.SEARCH_BOX_LOCATOR)

    def button_menu(self):
        return self.find(*YandexImagesLocators.BUTTON_MENU_LOCATOR)

    def go_to_images(self):
        self.search_box().click()
        self.button_menu().click()
        return self.find(*YandexImagesLocators.IMAGES_LOCATOR)

    def open_first_category(self):
        self.go_to_images().click()
        second_page = self.browser.window_handles[1]
        self.browser.switch_to.window(second_page)
        self.find(*YandexImagesLocators.FIRST_CATEGORY_LOCATOR).click()

    def category_in_search_box(self):
        return self.find(*YandexImagesLocators.CATEGORY_IN_SEARCH_BOX_LOCATOR)

    def select_first_image(self):
        self.open_first_category()
        return self.find(*YandexImagesLocators.FIRST_IMAGE_LOCATOR)

    def image_is_open(self):
        return self.find(*YandexImagesLocators.IMAGE_OPEN_LOCATOR)

    def forward(self):
        self.find(*YandexImagesLocators.FORWARD_BUTTON_LOCATOR).click()

    def back(self):
        self.find(*YandexImagesLocators.BACK_BUTTON_LOCATOR).click()

    def list_of_images(self):
        return self.browser.find_elements(*YandexImagesLocators.FIRST_IMAGE_LOCATOR)
