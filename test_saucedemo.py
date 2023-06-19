from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
URL = "https://www.saucedemo.com/"

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    return driver

def open_login_page(driver, our_url):
    driver.get(our_url)

def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)

def click_element_by_id(driver, locator):
    driver.find_element(By.ID, locator).click()

def element_send_keys(driver, locator, key):
    elem = get_element_by_id(driver, locator)
    elem.send_keys(key)

def login(driver, name, password):
    element_send_keys(driver, "user-name", USERNAME)
    element_send_keys(driver, "password", PASSWORD)
    click_element_by_id(driver, "login-button")


driver = get_driver()
open_login_page(driver, URL)
login(driver=driver, name=USERNAME, password=PASSWORD)

driver.quit()