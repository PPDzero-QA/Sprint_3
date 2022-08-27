import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver

from locators import *

url = "https://stellarburgers.nomoreparties.site/"


class TestRegistration():
    def test_registration_valid_data(self):
        driver = webdriver.Chrome()

        driver.get(url + "register")
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, RegLocators.reg_input_name)))
        driver.find_element(By.XPATH, RegLocators.reg_input_name).send_keys('Ruslan')
        driver.find_element(By.XPATH, RegLocators.reg_input_email).send_keys('ruslan-sab122clear11@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.reg_input_password).send_keys('1qaz2WSX')
        driver.find_element(By.XPATH, RegLocators.reg_button_submit).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_button_login)))
        assert driver.current_url == url + "login"

    def test_registration_password_less_than_6_characters_text_incorrect_password(self):
        driver = webdriver.Chrome()

        driver.get(url + "register")
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, RegLocators.reg_input_name)))
        driver.find_element(By.XPATH, RegLocators.reg_input_name).send_keys('Ruslan')
        driver.find_element(By.XPATH, RegLocators.reg_input_email).send_keys('ruslan-sab1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.reg_input_password).send_keys('1qaz')
        driver.find_element(By.XPATH, RegLocators.reg_button_submit).click()

        WebDriverWait(driver, 3).until(ec.presence_of_element_located((By.XPATH, RegLocators.reg_text_invalid_password)))
        assert driver.find_element(By.XPATH, RegLocators.reg_text_invalid_password)


class TestAuthorization:
    def test_auth_by_log_in_to_account_button_in_the_main_page(self):
        driver = webdriver.Chrome()

        driver.get(url)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_button_login)))
        driver.find_element(By.XPATH, MainLocators.main_button_login).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_input_email)))
        driver.find_element(By.XPATH, AuthLocators.auth_input_email).send_keys('ruslansab11220@yandex.ru')
        driver.find_element(By.XPATH, AuthLocators.auth_input_password).send_keys('1qaz2wsx')
        driver.find_element(By.XPATH, AuthLocators.auth_button_login).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_button_place_an_order)))
        assert driver.find_element(By.XPATH, MainLocators.main_button_place_an_order)

    def test_auth_by_personal_account_button_in_the_main_page(self):
        driver = webdriver.Chrome()

        driver.get(url)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_personal_account_header)))
        driver.find_element(By.XPATH, MainLocators.main_personal_account_header).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_input_email)))
        driver.find_element(By.XPATH, AuthLocators.auth_input_email).send_keys('ruslansab11220@yandex.ru')
        driver.find_element(By.XPATH, AuthLocators.auth_input_password).send_keys('1qaz2wsx')
        driver.find_element(By.XPATH, AuthLocators.auth_button_login).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_button_place_an_order)))
        assert driver.find_element(By.XPATH, MainLocators.main_button_place_an_order)

    def test_auth_by_login_button_in_the_registration_page(self):
        driver = webdriver.Chrome()

        driver.get(url + 'register')
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, RegLocators.reg_link_login)))
        driver.find_element(By.XPATH, RegLocators.reg_link_login).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_input_email)))
        driver.find_element(By.XPATH, AuthLocators.auth_input_email).send_keys('ruslansab11220@yandex.ru')
        driver.find_element(By.XPATH, AuthLocators.auth_input_password).send_keys('1qaz2wsx')
        driver.find_element(By.XPATH, AuthLocators.auth_button_login).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_button_place_an_order)))
        assert driver.find_element(By.XPATH, MainLocators.main_button_place_an_order)

    def test_auth_by_login_button_in_the_forgot_password_page(self):
        driver = webdriver.Chrome()

        driver.get(url + 'forgot-password')
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, RegLocators.reg_link_login)))
        driver.find_element(By.XPATH, RegLocators.reg_link_login).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_input_email)))
        driver.find_element(By.XPATH, AuthLocators.auth_input_email).send_keys('ruslansab11220@yandex.ru')
        driver.find_element(By.XPATH, AuthLocators.auth_input_password).send_keys('1qaz2wsx')
        driver.find_element(By.XPATH, AuthLocators.auth_button_login).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_button_place_an_order)))
        assert driver.find_element(By.XPATH, MainLocators.main_button_place_an_order)


class TestLogout:
    def test_logout_by_logout_button_in_the_personal_account_page(self):
        driver = webdriver.Chrome()

        driver.get(url + 'login')

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_input_email)))
        driver.find_element(By.XPATH, AuthLocators.auth_input_email).send_keys('ruslansab11220@yandex.ru')
        driver.find_element(By.XPATH, AuthLocators.auth_input_password).send_keys('1qaz2wsx')
        driver.find_element(By.XPATH, AuthLocators.auth_button_login).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_personal_account_header)))
        driver.find_element(By.XPATH, MainLocators.main_personal_account_header).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.personal_account_button_logout)))
        driver.find_element(By.XPATH, MainLocators.personal_account_button_logout).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_button_login)))
        assert driver.find_element(By.XPATH, AuthLocators.auth_button_login)


class TestPersonalAccountAndConstructor:
    def test_go_to_personal_account_page(self):
        driver = webdriver.Chrome()

        driver.get(url + 'login')
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_input_email)))
        driver.find_element(By.XPATH, AuthLocators.auth_input_email).send_keys('ruslansab11220@yandex.ru')
        driver.find_element(By.XPATH, AuthLocators.auth_input_password).send_keys('1qaz2wsx')
        driver.find_element(By.XPATH, AuthLocators.auth_button_login).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_personal_account_header)))
        driver.find_element(By.XPATH, MainLocators.main_personal_account_header).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.personal_account_button_logout)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' and driver.find_element(By.XPATH, MainLocators.personal_account_button_logout)

    def test_go_to_the_constructor_page_from_personal_account_by_logo_сlick(self):
        driver = webdriver.Chrome()

        driver.get(url + 'login')
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_input_email)))
        driver.find_element(By.XPATH, AuthLocators.auth_input_email).send_keys('ruslansab11220@yandex.ru')
        driver.find_element(By.XPATH, AuthLocators.auth_input_password).send_keys('1qaz2wsx')
        driver.find_element(By.XPATH, AuthLocators.auth_button_login).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_personal_account_header)))
        driver.find_element(By.XPATH, MainLocators.main_personal_account_header).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_logo_header)))
        driver.find_element(By.XPATH, MainLocators.main_logo_header).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_tab_menu_buns)))
        assert driver.find_element(By.XPATH, MainLocators.main_tab_menu_buns)

    def test_go_to_the_constructor_page_from_personal_account_by_constructor_button(self):
        driver = webdriver.Chrome()

        driver.get(url + 'login')
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, AuthLocators.auth_input_email)))
        driver.find_element(By.XPATH, AuthLocators.auth_input_email).send_keys('ruslansab11220@yandex.ru')
        driver.find_element(By.XPATH, AuthLocators.auth_input_password).send_keys('1qaz2wsx')
        driver.find_element(By.XPATH, AuthLocators.auth_button_login).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_personal_account_header)))
        driver.find_element(By.XPATH, MainLocators.main_personal_account_header).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_logo_header)))
        driver.find_element(By.XPATH, MainLocators.main_logo_header).click()

        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_tab_menu_buns)))
        assert driver.find_element(By.XPATH, MainLocators.main_tab_menu_buns)

    def test_navigation_to_buns_in_the_constructor(self):
        driver = webdriver.Chrome()

        driver.get(url)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_tab_menu_buns)))

        element = driver.find_element(By.XPATH, MainLocators.main_last_element_in_the_constructor)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        driver.find_element(By.XPATH, MainLocators.main_tab_menu_buns).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.main_title_buns)

    def test_navigation_to_sauces_in_the_constructor(self):
        driver = webdriver.Chrome()

        driver.get(url)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_tab_menu_sauces)))

        element = driver.find_element(By.XPATH, MainLocators.main_last_element_in_the_constructor)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        driver.find_element(By.XPATH, MainLocators.main_tab_menu_sauces).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.main_title_sauces)

    def test_navigation_to_fillings_in_the_constructor(self):
        driver = webdriver.Chrome()

        driver.get(url)
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, MainLocators.main_tab_menu_fillings)))

        driver.find_element(By.XPATH, MainLocators.main_tab_menu_fillings).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.main_title_fillings)
