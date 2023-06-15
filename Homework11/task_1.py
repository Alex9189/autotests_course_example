# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
try:
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'неверно открыт сайт'
    assert driver.title == sbis_title, 'неверный заголовок'
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, 'Должно быть 4 вкладки'

    contacts_btn = driver.find_element(By.LINK_TEXT, 'Контакты') # ищем кнопку по названию ссылки
    # contacts_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Button--primary')
    # contacts_btn.txt = 'Начать работу'
    # assert contacts_btn.text == contacts_btn.txt
    # assert contacts_btn.get_attribute('title') == contacts_btn.txt
    # assert contacts_btn.is_displayed()
    contacts_btn.click()
    sleep(1)
    # banner_btn = driver.find_element(By.CSS_SELECTOR, '.contacts_clients > div.sbis_ru-container > div > div > div.s-Grid-col.s-Grid-col--4 > div > a > img')

    # banner_btn = driver.find_elements(By.CSS_SELECTOR, '.s-Grid-col [src="/resources/NewDesign/pages/Contacts/images/logo.svg?x_module=23.3206-53"]')
    banner_btn = driver.find_elements(By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    banner_item = banner_btn[0]
    banner_item.click()
    driver.switch_to.window(driver.window_handles[1])

    Power_title = driver.find_element(By.XPATH, ' //p[text()="Сила в людях"]')
    assert Power_title.text == 'Сила в людях'

    about = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    assert about.text == 'Подробнее'
    about.location_once_scrolled_into_view
    about.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Неверный адрес сайта'
finally:
    driver.quit()
