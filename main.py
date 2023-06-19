from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
username = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
# найти поле имени пользователя / электронной почты и отправить само имя пользователя в поле ввода
driver.find_element(By.ID, "user-name").send_keys(username)
# найти поле ввода пароля и также вставить пароль
driver.find_element(By.ID, "password").send_keys(password)
# нажмите кнопку входа в систему
driver.find_element(By.ID, "login-button").click()

# ждем завершения состояния готовности
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# получаем ошибки (если есть)
errors = driver.find_elements(By.CLASS_NAME, "error")
# при необходимости распечатать ошибки
# для e в ошибках:
#     print(e.text)
# если мы находим это сообщение об ошибке в составе error, значит вход не выполнен
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

driver.close()

print("Mew")