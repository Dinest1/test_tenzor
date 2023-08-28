from selenium.webdriver.common.by import By


class YandexSearchLocators:
    SEARCH_BOX_LOCATOR = (By.CSS_SELECTOR, '.search3__input.mini-suggest__input')
    SUGGEST_LOCATOR = (By.CSS_SELECTOR, '.mini-suggest_open')
    BUTTON_SUBMIT_LOCATOR = (By.CSS_SELECTOR, '.search3__button.mini-suggest__button')
    SEARCH_RESULT_LOCATOR = (By.CSS_SELECTOR, '#search-result')
    SEARCH_LINK_LOCATOR = (By.CSS_SELECTOR, 'div.Path.Organic-Path.Organic-Path_verified.path.organic__path > a.Link')


class YandexImagesLocators:
    SEARCH_BOX_LOCATOR = (By.CSS_SELECTOR, '.search3__input.mini-suggest__input')
    BUTTON_MENU_LOCATOR = (By.CSS_SELECTOR, '[data-statlog="services_suggest.more"]')
    IMAGES_LOCATOR = (By.CSS_SELECTOR, '[data-statlog="services-more-popup.item.images"]')
    FIRST_CATEGORY_LOCATOR = (By.CSS_SELECTOR, 'div.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a')
    CATEGORY_IN_SEARCH_BOX_LOCATOR = (By.CSS_SELECTOR, 'form.mini-suggest_has-value_yes')
    FIRST_IMAGE_LOCATOR = (By.CSS_SELECTOR, 'a.serp-item__link')
    IMAGE_OPEN_LOCATOR = (By.CSS_SELECTOR, 'div.Modal_visible')
    FORWARD_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'div.CircleButton_type_next > i')
    BACK_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'div.CircleButton_type_prev > i')