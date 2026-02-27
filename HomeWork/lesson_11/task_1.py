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


saby_site = 'https://saby.ru/'
saby_site_contacts = 'https://saby.ru/contacts/76-yaroslavskaya-oblast?tab=clients'
tensor_site = 'https://tensor.ru/'
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Переходим на сайт саби
    driver.get(saby_site)
    sleep(2)
    assert driver.current_url == saby_site, 'А сайт то не тот'
    # Переходим в раздел Контакты
    contacts_button = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"].sbisru-Footer__link')
    assert contacts_button.text == 'Контакты', 'Это кнопка не раздела Контакты'
    assert contacts_button.is_displayed(), 'Кнопка пропала!'
    contacts_button.click()
    assert driver.current_url == saby_site_contacts, 'Не перешли в раздел Контакты'
    # Ищем логотип Тензора и кликаем по нему
    contacts_section = driver.find_element(By.CSS_SELECTOR, '[id="contacts_clients"] a[href="https://tensor.ru/"]')
    sleep(2)
    contacts_section.click()
    # Переключаемся на вторую вкладку
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == tensor_site, 'Не перешли на сайт Тензора'
    # Ищем блок с новостями
    block_news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-Index__card-title')
    assert block_news.text == 'Сила в людях', 'Нет блока новостей с таким названием'
    more_button = block_news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-link')
    assert more_button.is_displayed(), 'Нет кнопки подробнее!'
    # Переходим в раздел "О компании" по клику на "Подробнее"
    more_button.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Не перешли на вкладку \"О компании\"'
    sleep(2)
finally:
    driver.quit()
