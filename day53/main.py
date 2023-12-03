from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

LINK = "https://www.zillow.com/philadelphia-pa/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A40.14359325281126%2C%22east%22%3A-74.95251833203127%2C%22south%22%3A39.834782695046684%2C%22west%22%3A-75.4922217011719%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13271%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A11%7D"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdAXYtl5PLAZUhdVWU23Zkajw3A-cX3z8555e0AJ5_coGD60A/viewform?usp=sf_link"

service = ChromeService(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url=LINK)

addresses = []

#
# for address in driver.find_element(By.CLASS_NAME,'StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link'):
#     addresses.append(address.text)

print(driver.text)




# driver.get(url=FORM_LINK)
# time.sleep(2)
# address = driver.find_element(By.XPATH,
#                               "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
# address.click()
# address.send_keys("addressn")
# time.sleep(1)
# price = driver.find_element(By.XPATH,
#                             '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# price.click()
# price.send_keys("pricen")
# time.sleep(1)
# link = driver.find_element(By.XPATH,
#                            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
# link.click()
# link.send_keys("linkn")
# time.sleep(1)
# submit = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
# submit.click()
# time.sleep(3)




