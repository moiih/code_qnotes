from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pathlib import Path
import schedule
import time
import sys
import os


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))  # loading the environment variable(.env) file

def run_script():
    print('-----------------------\nEntered into the run_script()\n-----------------------')

    target_username = os.getenv('username')
    target_password = os.getenv('password')

    url = "https://mohits23.pythonanywhere.com/login/"


    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get(url)

    driver.find_element(By.NAME, "username").send_keys(target_username)
    driver.find_element(By.NAME, "password").send_keys(target_password)
    driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
    print("-----------------------\nLogged in successfully !!\n------------------------")
    time.sleep(3)

    driver.get("https://mohits23.pythonanywhere.com/user_profile/12")
    time.sleep(3)

    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    driver.implicitly_wait(35)

    driver.find_element(By.ID, "remove_post25").click()
    #driver.find_element(By.CLASS_NAME, "rem_post25").click()
    #del_button = driver.find_element(By.ID, "remove_post25")
    #driver.implicitly_wait(10)
    #del_button.click()
    time.sleep(4)

    print("-----------------------\nPost deleted successfully !!\n------------------------")
    # breakpoint()  ## To pause the Chrome Window

    driver.quit()
    sys.exit()



# To get the time of 5 seconds ahead
extended_time = datetime.now() + timedelta(seconds=5)
list_time = list(str(extended_time))
#print(list_time)
#print()

t_time = list_time[11:19]
#print(t_time)

s_time = ''.join(t_time)
print('Time+5sec =', s_time)

## To Schedule the above script by 's_time'
schedule.every().day.at(s_time).do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)

#time.sleep(5)
#input()
