import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

MY_USERNAME = "dhalttt"
MY_PASSWORD = "DHalttt.insta"

service = ChromeService(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#open instagram and login
driver.get(url="https://www.instagram.com/")
time.sleep(3)
username = driver.find_element(By.NAME, "username")
username.click()
username.send_keys(MY_USERNAME)
password = driver.find_element(By.NAME, "password")
password.click()
password.send_keys(MY_PASSWORD)
time.sleep(1)
password.send_keys(Keys.ENTER)
time.sleep(10)
#find the user to follow others

driver.switch_to.new_window()
driver.get(url="https://www.instagram.com/dualipa")
time.sleep(5)
dua_followers = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div')
dua_followers.click()

time.sleep(2)
# follow = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[3]/button')
# follow.click()

