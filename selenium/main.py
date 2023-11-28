import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

webdriver_service = Service(f"/home/ohmmaagoch/python-playground/selenium/chromedriver/stable/chromedriver")

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

browser.get("www.google.com")
time.sleep(10)

browser.quit()
