import ctypes
import os
import time
import random
import configparser
from colorama import Fore, Style, init
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# Colorama ANSI Conversion
init(convert=True, autoreset=True)
# File Configuration
file_exists = os.path.isfile('settings.txt')
if file_exists:
    exists = 1
else:
    f = open("settings.txt", "w")

configParser = configparser.RawConfigParser()
configFilePath = r'settings.txt'
configParser.read(configFilePath)

# Console Heading
# ctypes.windll.kernel32.SetConsoleTitleW("Pearson AutoETextReader | by sleepymountain")
print(f"{Fore.LIGHTRED_EX}AutoETextReader {Style.RESET_ALL}v1.00 | {Fore.LIGHTYELLOW_EX}By sleepymountain")
print("\n")

# User Configuration
settings_load_prompt = input("Load Settings from File? [y/n]")
if settings_load_prompt.lower() == "y":
    page = configParser.get('Page-Settings', 'starting_page')
    int_page = int(page)
    max_page = configParser.get('Page-Settings', 'ending_page')
    int_max_page = int(max_page)
    wait_range_min = configParser.get('Page-Settings', 'min_page_time')
    wait_range_max = configParser.get('Page-Settings', 'max_page_time')
    e_text = configParser.get('Pearson-Settings', 'e_text_link')
    username = configParser.get('Pearson-Settings', 'login_username')
    password = configParser.get('Pearson-Settings', 'login_password')
    print(f"{Fore.LIGHTGREEN_EX}[!] Loaded settings.txt{Style.RESET_ALL}")
elif settings_load_prompt.lower() == "n":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Page Settings ---")
    page = input("Starting Page Number: ")
    int_page = int(page)
    max_page = input("Ending Page Number: ")
    int_max_page = int(max_page)
    wait_range_min = input("Minimum Page Read Time: ")
    wait_range_max = input("Maximum Page Read Time: ")
    print("\n")
    print(f"{Fore.LIGHTGREEN_EX}[!] Open Your EText to Page: i (Title Page) and Copy the Link{Style.RESET_ALL}")
    print("\n")
    e_text = input("Pearson EText Link: ")  # Need to Make Sure pagenumber=i
    print("\n")
    print("--- Login Settings ---")
    username = input("Pearson Login Username: ")
    password = input("Pearson Login Password: ")
    # settings_save_prompt = input("Save Settings to File? [y/n]")

# WebDriver Setup
os.system('cls' if os.name == 'nt' else 'clear')
input(f"{Fore.LIGHTBLUE_EX}Press Enter to start...{Style.RESET_ALL}")
print(f"{Fore.LIGHTBLUE_EX}[#] Loading reader.{Style.RESET_ALL}.")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-extensions");
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('resources\chromedriver.exe', options=options)
actions = ActionChains(driver)

# cont. reader
print(f"{Fore.LIGHTGREEN_EX}[!] Reader Loaded{Style.RESET_ALL}")
os.system('cls' if os.name == 'nt' else 'clear')
# Visits EText Link
print(f"{Fore.LIGHTBLUE_EX}[#] Loading EText..{Style.RESET_ALL}")
e_text_page = e_text.replace("pagenumber=i", "pagenumber=" + page)
driver.get(e_text_page)
time.sleep(5)

# Finds Login Elements and Inputs User-Defined Information
driver.find_elements_by_xpath('//*[@id="username"]')[0].send_keys(username)
driver.find_elements_by_xpath('//*[@id="password"]')[0].send_keys(password)
time.sleep(5)
driver.find_elements_by_xpath('//*[@id="mainButton"]')[0].click()
time.sleep(5)
# Check if Login Information is Invalid
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{Fore.LIGHTBLUE_EX}[#] Logging in..{Style.RESET_ALL}")
incorrect_login_text = "That username or password didn't work."
if incorrect_login_text in driver.page_source:
    print(f"{Fore.RED}[x] Incorrect login information. Process will quit.{Style.RESET_ALL}")
    time.sleep(5)
    exit()
else:
    print(f"{Fore.LIGHTGREEN_EX}[!] Login successful!{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLUE_EX}[#] Waiting to start..{Style.RESET_ALL}")
    time.sleep(30)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.LIGHTBLUE_EX}[#] Starting reader..{Style.RESET_ALL}")
    # Waits Random Amount of Time Between User-Defined Integers and Proceeds to Next Page
    start = time.time()
    while int_page < int_max_page:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTGREEN_EX}[!] Reading...{Style.RESET_ALL}")
        page_rand = random.randrange(int(wait_range_min), int(wait_range_max))
        print(f"{Fore.LIGHTGREEN_EX}[i] Current Page: " + str(int_page) + "/" + str(int_max_page) + f"{Style.RESET_ALL}")
        time.sleep(page_rand)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
        int_page = int_page + 1
        print(f"{Fore.LIGHTBLUE_EX}>> Next Page >>{Style.RESET_ALL}")

# Runs when Reader is Complete
    if int_page == int_max_page:
        end = time.time()
        elapsed = end - start
        print(f"{Fore.LIGHTGREEN_EX}[!] Reading Complete!{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}[i] Pages: {Style.RESET_ALL}" + str(int_page) + "/" + str(int_max_page))
        print(f"{Fore.LIGHTBLUE_EX}[i] Elapsed Time: {Style.RESET_ALL}" + str(elapsed) + "s")
        input(f"{Fore.LIGHTRED_EX}Press Enter to exit.{Style.RESET_ALL}")
        exit()


