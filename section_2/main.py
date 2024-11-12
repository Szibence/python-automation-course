from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('D:\\software_projects\\chromedriver-win64\\chromedriver.exe')

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(" ")[-1])
    return output

def main():
    driver = get_driver()
    time.sleep(2)

    element_quote = driver.find_element(By.XPATH, value="/html/body/div[1]/div/h1[1]")
    text_quote = element_quote.text

    element_temperature = driver.find_element(By.XPATH, value="/html/body/div[1]/div/h1[2]")
    text_temperature = clean_text(element_temperature.text)

    # driver.quit()

    return text_temperature

    
print(main())