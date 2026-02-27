# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


now = datetime.now()
current_date = now.strftime('%Y-%m-%d')

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

my_name = 'Сергеев Сергей Альбертович'
text_message = 'Хватит писать самому себе письма, выглядишь как жизофреник!'
site = 'https://fix-online.sbis.ru'
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
action_chains = ActionChains(driver)

try:
    driver.get(site)

    # Тут динамический атрибут у тэга, текущая дата
    # Вводим логин
    login = driver.find_element(By.CSS_SELECTOR, f'.auth-AdaptiveLoginForm__inputBlock [name="ws-input_{current_date}"]')
    login.send_keys('asus', Keys.ENTER)
    assert login.get_attribute('value') == 'asus', 'Не правильный логин'

    # Вводим пароль
    password = driver.find_element(By.CSS_SELECTOR, f'.auth-AdaptiveLoginForm__password [name="ws-input_{current_date}"]')
    password.send_keys('asus43210', Keys.ENTER)

    # Ждём появлкения аккордеона
    accordion_items = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')
    ))

    # Перебираем вкладки аккордеона и ищем "Контакты"
    contacts = ''
    for item in accordion_items:
        if item.text == 'Контакты':
            contacts = item
            break
    assert contacts != '', 'Вкладка не найдена'

    # Перемещаем курсор и кликаем по "Контакты"
    action_chains.move_to_element(contacts).double_click(contacts).perform()

    # Ждём появления кнопки Написать письмо и кликаем
    add_message = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.sabyPage-MainLayout__headerLeft [data-qa="sabyPage-addButton"]')
    ))
    add_message.click()

    # Ищем поле адресата и вводим своё имя
    search_me = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, f'.controls-StackTemplate-content [name="ws-input_{current_date}"]')
    ))
    action_chains.click(search_me).send_keys(my_name).perform()
    search_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-qa="Search__searchButton"]')
    ))
    search_button.click()
    # Выбираем себя как адресата
    iam_recipients = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.person-BaseInfo__highlightContainer_Highlight')
    ))
    iam_recipients.click()

    # Ищем поле ввода и набираем тексст письма
    editor_field = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    ))
    action_chains.click(editor_field).send_keys(text_message).perform()

    # Ищем и кликаем кнопку отправить письмо
    send_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_message.click()
    sleep(2)
    # Проссматриваем все письма и ищём наш текст
    letters = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '.msg-dialogs-item__message-text')
    ))

    for item in letters:
        if item.text == text_message:
            print('Нам пришло письмо')
            action_chains.move_to_element(item).context_click(item).perform()
            del_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.controls-Menu__content[title = "Перенести в удаленные"]')
            ))
            action_chains.move_to_element(del_button).click().perform()

    # Проверяем удалено ли письмо из реестра

    letters2 = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '.msg-dialogs-item__message-text')
    ))
    count = 0
    for item2 in letters2:
        if item2.text == text_message:
            count += 1

    assert count == 0, 'Письмо не удалили'
    print('Письмо удалено из реестра контактов')
finally:
    driver.quit()
