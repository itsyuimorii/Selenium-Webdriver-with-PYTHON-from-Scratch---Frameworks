
from datetime import time
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def main():
    service = Service('/Users/itsyuimoriispace/Downloads/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(service=service)

    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

    driver.find_element(By.ID, 'autosuggest').send_keys('ca')
    time.sleep(2)
    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
    print(len(countries))




if __name__ == '__main__':
    main()
