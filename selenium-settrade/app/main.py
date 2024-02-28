from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def get_element_by_xpath(driver :WebDriver, xpath: str):
    return driver.find_element(By.XPATH, xpath)

def open_web_by_stock_name(driver: WebDriver, name: str):
    ...

def get_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('/driver/chromedriver')
    return chrome_options

def main():
    try:
        URL="https://www.settrade.com/th/home"
        chrome_option = get_chrome_options()
        driver = webdriver.Chrome(options=chrome_option)
        wait = WebDriverWait(driver=driver, timeout=3)

        driver.get(URL)

        ads_btn = driver.find_element(By.XPATH, "//*[@id='modalFloatingAds']/div/div[1]/button")
        wait.until(lambda d: ads_btn.is_displayed())
        ads_btn.click()

        search_bar = driver.find_element(By.XPATH, "//*[@id='appbar']/div[1]/div[2]/div/div/div[1]")
        wait.until(lambda d: search_bar.is_displayed())
        search_bar.click()

        input_stock_name = driver.find_element(By.XPATH,"//*[@id='appbar']/div[1]/div[2]/div/div/div[1]/div[1]/input")
        wait.until(lambda d: input_stock_name.is_displayed)
        input_stock_name.click()
        input_stock_name.send_keys("PTT" + Keys.ENTER)

        # driver.find_element(By.XPATH, "//*[@id='swipertewnuc617i']/div/div[1]/a[4]").click()
        sleep(10)

    except Exception as e:
        print("Error -> ", e)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
