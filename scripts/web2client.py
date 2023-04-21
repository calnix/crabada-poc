from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
from scripts.helpful_scripts import (MM_login, is_total_expeditions_present, expedition_check,get_timeLeft)
from datetime import datetime

def load_brower():
## --------------- Setup Engine ---------------------##
    chromeDriverPath = r"D:\p2e\chromedriver_win32\chromedriver.exe"
    user_data_dir = r"D:\p2e\User Data"  # TELL WHERE IS THE DATA DIR
    profile_dir = (r"Profile 1")  # chrome user profile path -> chrome://version/   | e.g. profile 3

    chrome_options = Options()
    desired_cap = chrome_options.to_capabilities()
    desired_cap.update({"browser": "chrome", "os": "Windows", "os_version": "10"})

    # chrome_options.add_argument(r"--user-data-dir=C:\Users\You\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument(r"--user-data-dir={}".format(user_data_dir))
    chrome_options.add_argument(r"--profile-directory={}".format(profile_dir))  

    #headless need xvfb (not available on windows)
    # https://stackoverflow.com/questions/45372066/is-it-possible-to-run-google-chrome-in-headless-mode-with-extensions/45372648#45372648
    #from pyvirtualdisplay import Display
    #display = Display(visible=0, size=(1920, 1200))
    #display.start()

    # Instantiate the webdriver
    browser = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=chrome_options)
    browser.get("https://play.crabada.com/mine")
    browser.maximize_window()
    # Save the window opener (current window, do not mistaken with tab... not the same)
    main_window = browser.current_window_handle  # shld be window_handles[0]
    print(f"..... This is main window: {main_window} .....")

    MM_login(browser)

    browser.switch_to.window(browser.window_handles[0])
    browser.execute_script("location.reload(true);")
    time.sleep(5)
    return browser


def game_state(browser):
    # get Total Mining Expedition(s)
    browser.switch_to.window(browser.window_handles[0])
    browser.execute_script("location.reload(true);")
    time.sleep(5)
    is_total_expeditions_present(browser)
    curr_expeditions = expedition_check(browser)
    print(f".... Number of Mining Expeditions {curr_expeditions} ....")
    return curr_expeditions

def get_miningID(browser):
        # Find mine number / gameid
        mining_id_title = browser.find_element(By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div[2]/div/div/div[2]/div[1]/h5').text
        mining_id = mining_id_title.split(" ")[1]
        print(f"...The mining id is {mining_id}...")
        return mining_id

def sleep_catch(browser):
    #timeleft - safety catchall 
    time_left_seconds = get_timeLeft(browser)
    print(f"<<<< Sleeping for {time_left_seconds} seconds >>>>")
    time.sleep(time_left_seconds)

def timenow():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


