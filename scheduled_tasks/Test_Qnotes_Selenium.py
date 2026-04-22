from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

target_username = "acer"
target_password = "abcd@123"

url = "https://qnotes23.pythonanywhere.com/authentication/"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
#driver.maximize_window()  ## To Maximize Chome Window
driver.get(url)


driver.find_element(By.NAME, "username").send_keys(target_username)
driver.find_element(By.NAME, "password").send_keys(target_password)
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()
time.sleep(2)

print("-----------------------\nLogged in successfully !!\n------------------------")


# breakpoint()  ## To pause the Chrome Window

driver.quit()

