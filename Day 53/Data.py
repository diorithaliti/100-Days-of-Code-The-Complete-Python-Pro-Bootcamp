import requests as requests
from bs4 import BeautifulSoup
LINK = "https://www.zillow.com/philadelphia-pa/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A40.14359325281126%2C%22east%22%3A-74.95251833203127%2C%22south%22%3A39.834782695046684%2C%22west%22%3A-75.4922217011719%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13271%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A11%7D"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}



class GetDataFromZillow():

    def __init__(self):
        self.response = requests.get(url=LINK, headers=HEADERS)
        self.content = self.response.text
        self.soup = BeautifulSoup(self.content, "html.parser")
        self.links = []
        self.prices = []
        self.address = []


    def get_address(self):
        for address in self.soup.find_all(
                class_='StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link'):
            self.address.append(address.text)
        return self.address

    def get_price(self):
        for price in self.soup.find_all(class_='StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX'):
            self.prices.append(price.text)
        return self.prices


    def get_link(self):
        for link in self.soup.find_all(
                class_='StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link'):
            self.links.append(f"https://www.zillow.com{link.get('href')}")
        return self.links




