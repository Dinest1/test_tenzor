import pytest
from pages.yandex_images import YandexImages


@pytest.mark.menu
def test_menu_button(browser):
    page = YandexImages(browser)
    page.open()
    page.search_box().click()
    assert page.button_menu()


@pytest.mark.images_category
def test_go_to_images(browser):
    page = YandexImages(browser)
    page.open()
    images_page = page.go_to_images()
    images_page.click()
    assert images_page.get_attribute('href') == 'https://ya.ru/images/'


@pytest.mark.first_category
def test_first_category(browser):
    page = YandexImages(browser)
    page.open()
    page.open_first_category()
    assert page.category_in_search_box()


@pytest.mark.images
def test_open_first_image(browser):
    page = YandexImages(browser)
    page.open()
    first_image = page.select_first_image()
    first_image.click()
    firs_image_link = first_image.get_attribute('href')
    assert page.image_is_open()

    page.forward()
    assert firs_image_link != page.list_of_images()[1].get_attribute('href')

    page.back()

    previous_image = page.list_of_images()[0].get_attribute('href')
    assert previous_image == firs_image_link


if __name__ == '__main__':
    pytest.main()


