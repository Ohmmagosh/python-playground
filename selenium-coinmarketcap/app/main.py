from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from rich import print as rprint, inspect as insp
from time import sleep
import csv
import math

def get_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('/driver/chromedriver')
    return chrome_options

def init_driver():
    chorme_options = get_chrome_options()
    driver = webdriver.Chrome(options=chorme_options)
    driver_wait = WebDriverWait(driver=driver, timeout=3)
    return driver , driver_wait

def get_coin_list_size(driver: WebDriver, url: str, wait: WebDriverWait) -> int:
    driver.get(url)
    coin_list = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[6]/span")
    # wait.until(coin_list, "coin list")
    coin_list = coin_list.text.split(' ')
    coin_list.reverse()
    return int(coin_list[0])

def scroll_page_down(driver: WebDriver):
    hight = driver.execute_script('return document.body.scrollHeight')
    stop_text = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[6]/div[2]/div/span")
    stop_text_y = stop_text.location['y']
    p_client_hight = hight - stop_text_y
    for i in range(0, hight, 5):
            driver.execute_script(f"window.scrollTo(0, {i})")
            client_hight =driver.execute_script('return window.scrollY')
            if client_hight + p_client_hight > stop_text_y:
                break
            sleep(0.01)

def get_header_table(driver: WebDriver):
    URL = f"https://coinmarketcap.com/"
    driver.get(url=URL)
    table_head = driver.find_elements(By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/thead/tr")
    header = [data for data in table_head][0].text.split('\n')
    return header

def get_table_data(driver: WebDriver):
    table_row = driver.find_elements(By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr")
    data_row = [data.text.split('\n') for index ,data in enumerate(table_row) if data.text]
    return data_row

def create_csv_file(filename: str, data: list[list[str]]):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)

def main():
    try:
        driver, driver_wait = init_driver()
        coin_size = get_coin_list_size(driver=driver, url="https://coinmarketcap.com/", wait=driver_wait)
        page_size = math.ceil(coin_size / 100)

        table = []
        header = get_header_table(driver=driver)
        table.append(header)

        for i in range(1,3):
            URL = f"https://coinmarketcap.com/?page={i}"
            driver.get(url=URL)

            scroll_page_down(driver=driver)


            data_row = get_table_data(driver=driver)
            for data in data_row:
                table.append(data)

        create_csv_file("crpytodata.csv", table)
    except Exception as e:
        rprint('[red]Error -> ', e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
