from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#import subprocess
import schedule
import time
import sys

def run_script():
    print('-----------------------\nEntered into the run_script()\n-----------------------')
    # subprocess.run(["python", "F:\Trashshots\Scheduled_Program_Test\Test_Qnotes_Selenium.py"])

    target_username = "acer"
    target_password = "abcd@123"

    url = "https://qnotes23.pythonanywhere.com/authentication/"


    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()  ## To Maximize Chome Window
    driver.get(url)

    driver.find_element(By.NAME, "username").send_keys(target_username)
    driver.find_element(By.NAME, "password").send_keys(target_password)
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()
    time.sleep(2)

    print("\n-----------------------\nLogged in successfully !!\n------------------------\n")
    # breakpoint()  ## To pause the Chrome Window

    driver.quit()
    sys.exit()

## To Schedule the above script
schedule.every().day.at("20:31").do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)

#time.sleep(5)
#input()
