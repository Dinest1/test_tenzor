import pytest
from pages.yandex_main_page import YandexMainPage


@pytest.mark.search_box
def test_search_box(browser):
    page = YandexMainPage(browser)
    page.open()
    assert page.search_box().is_displayed(), 'Поле поиска отсутствует'


@pytest.mark.suggest
def test_suggest(browser):
    page = YandexMainPage(browser)
    page.open()
    page.enter_in_search_box()
    assert page.suggest_is_displayed(), 'Таблица с подсказками не появилась'


@pytest.mark.search_result
def test_search_result(browser):
    page = YandexMainPage(browser)
    page.open()
    page.enter_in_search_box()
    page.click_on_button_submit()
    assert page.search_result(), 'Страница с результатами поиска не появилась'


@pytest.mark.first_link
def test_first_link(browser):
    page = YandexMainPage(browser)
    page.open()
    page.enter_in_search_box()
    page.click_on_button_submit()
    assert page.search_link() == 'https://tensor.ru/', 'Ссылка не ведет на необходимый сайт'


if __name__ == '__main__':
    pytest.main()
