import time
# from selenium import webdriver
# import pytest
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# def test_open_page(driver):
#     driver.get('https://openweathermap.org/')
#     driver.maximize_window()
#     assert 'openweathermap' in driver.current_url
#     print(driver.current_url)
#
#
# def test_check_page_title(driver):
#     assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
#
#
# def test_fill_search_city_field(driver):
#     search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
#     search_city_field.send_keys('New York')
#     time.sleep(10)
#     search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
#     search_button.click()
#     driver.implicitly_wait(10)
#     search_option = driver.find_element(By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
#     search_option.click()
#     time.sleep(5)
#     expected_city = 'New York City, US'
#     displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
#     displayed_city_text = displayed_city.text
#     print(displayed_city_text)
#     assert displayed_city_text == expected_city


def test_log_in(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    time.sleep(10)
    log_in = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign in']"))
    )
    log_in.click()


def test_create_account(driver):

    create_account = driver.find_element(By.XPATH, '//a[text()="Create an Account."]')
    create_account.click()

    fill_username = driver.find_element(By.ID, 'user_username')
    fill_username.send_keys('Andrei')

    fill_email = driver.find_element(By.ID, 'user_email')
    fill_email.send_keys('test@test.com')

    fill_password = driver.find_element(By.ID, 'user_password')
    fill_password.send_keys('Testtest')

    fill_confirm_password = driver.find_element(By.ID, 'user_password_confirmation')
    fill_confirm_password.send_keys('Testtest')

    checkbox_years = driver.find_element(By.ID, 'agreement_is_age_confirmed')
    checkbox_years.click()

    checkbox_agreement = driver.find_element(By.ID, 'agreement_is_accepted')
    checkbox_agreement.click()

    checkbox_1 = driver.find_element(By.ID, 'mailing_system')
    checkbox_1.click()

    checkbox_2 = driver.find_element(By.ID, 'mailing_product')
    checkbox_2.click()

    checkbox_3 = driver.find_element(By.ID, 'mailing_news')
    checkbox_3.click()

    click_submit_btn = driver.find_element(By.CLASS_NAME, '.btn.btn-color.btn-submit')
    driver.execute_script("return arguments[0].scrollIntoView(true);", click_submit_btn)
    click_submit_btn.click()

    click_submit_btn = driver.find_element(By.CLASS_NAME, '.btn.btn-color.btn-submit')
    driver.execute_script("return arguments[0].scrollIntoView(true);", click_submit_btn)
    click_submit_btn.click()

    time.sleep(10)


def test_click_submit_button(driver):
    fill_email = driver.find_element(By.CLASS_NAME, 'string.email.optional.form-control')
    fill_email.send_keys('test')
    fill_password = driver.find_element(By.ID, '')
    time.sleep(2)
    click_submit = driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-default.btn-color')
    click_submit.click()
    message = driver.find_element(By.CLASS_NAME, 'panel-heading')
    assert message == 'Invalid Email or password.'
    time.sleep(2)



