import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions


options = ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome(options=options)
browser.get("https://bot.sannysoft.com/")
time.sleep(1000)


