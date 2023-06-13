# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'
try:
    driver.get(sbis_site)
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('том112', Keys.ENTER)
    assert login.get_attribute('value') == 'том112'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('AllStar9189', Keys.ENTER)
    sleep(5)

    contacts_btn = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    contacts_btn.click()
    sleep(2)
    contacts_btn.click()
    # action_chains = ActionChains(driver)
    # action_chains.double_click(contacts_btn)
    # # action_chains.move_to_element(contacts_btn)
    # action_chains.perform()
    # sleep(4)

    # contacts_title = driver.find_elements(By.CSS_SELECTOR, '.headTitle')
    # contacts_btn.click()
    # action_chains.double_click(contacts_btn)
    # action_chains.perform()
    sleep(4)

    plus_btn = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    plus_btn.click()
    sleep(2)

    string = driver.find_elements(By.CSS_SELECTOR, '.controls-Field')
    string[0].send_keys('том')
    sleep(2)

    my_name = driver.find_element(By.CSS_SELECTOR, '[title = "Брэди Том"]')
    my_name.click()
    sleep(2)

    string2 = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    pismo = 'Hallo mein lieber Freund!'
    string2.send_keys(pismo)
    sleep(2)

    send = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    send.click()
    sleep(2)

    # letter = driver.find_elements(By.XPATH, '// a[text() = "Hallo mein lieber Freund!"]')
    # letter = driver.find_elements(By.TAG_NAME, ('div.p'))
    letter = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-content')
    letter_fi = letter[0].text
    assert letter_fi[3:] == pismo, 'неверный текст письма'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(letter[0])
    action_chains.perform()
    sleep(2)

    delete = driver.find_elements(By.CSS_SELECTOR, '.controls-BaseButton .icon-Erase')
    delete[0].click()
    sleep(5)
    # letter[0].click()
    # print('Авторизоваться')
    # sleep(1)
    # user_login, user_password = 'discus_admin1', 'discus_admin123'
    # login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    # login.send_keys(user_login, Keys.ENTER)
    # assert login.get_attribute('value') == user_login
    # sleep(1)
    # password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    # password.send_keys(user_password, Keys.ENTER)
finally:
    driver.quit()