from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = ChromeService(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url="https://tinder.com/app/recs")

login = driver.find_element(By.XPATH, '//*[@id="q1623655810"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(5)
login_fb = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
login_fb.click()

time.sleep(60)
can_swipe = 0
while can_swipe < 20:
    like = driver.find_element(By.XPATH, '//*[@id="q1623655810"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span')
    like.click()
    time.sleep(5)

    can_swipe += 1