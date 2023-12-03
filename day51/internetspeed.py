from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MY_MAIL = "dhalttt@gmail.com"
MY_PASSWORD = "dhalttt@gmail"


class ISandTweet:

    def __init__(self):
        self.service = ChromeService(executable_path="C:\Development\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)



    def get_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        start = self.driver.find_element(By.XPATH,
                                    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        time.sleep(40)
        download = self.driver.find_element(By.XPATH,
                                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        upload = self.driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        return f"Download: {download.text}, Upload: {upload.text}"


    def tweet(self):
        speed = self.get_speed()
        self.driver.get(url="https://twitter.com")
        time.sleep(5)
        sign_in = self.driver.find_element(By.XPATH,
                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()
        time.sleep(5)
        email = self.driver.find_element(By.XPATH,
                                    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label')
        email.click()
        email.send_keys(MY_MAIL)
        email.send_keys(Keys.ENTER)
        # username and password
        time.sleep(2)
        user = self.driver.find_element(By.NAME, 'text')
        user.send_keys("dhalttt")
        user.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(MY_PASSWORD)
        password.send_keys(Keys.ENTER)

        # compose a tweet
        time.sleep(5)
        compose = self.driver.find_element(By.XPATH,
                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        compose.click()
        compose.send_keys(f" My internet speed : {speed}")
        tweet = self.driver.find_element(By.XPATH,
                                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()

