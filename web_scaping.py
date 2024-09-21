from localizator import *
from routs import *
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Web_Scrapping:

    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)

    def read_price(self, field):
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(field))
        return self.driver.find_element(*field).text
    
    def press_button(self, field):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(field))
        self.driver.find_element(*field).click()
    

class Swp_page:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def gold_prices(self):
        gold_price_funct = Web_Scrapping(self.driver, swp_gold_rout)
        time.sleep(10)
        gold_price_funct.press_button(button_display_field)
        time.sleep(10)
        gold_price_funct.press_button(button_24_display_field)
        print(gold_price_funct.read_price(gold_price_field))
        print(gold_price_funct.read_price(silver_price_field))

        print(gold_price_funct.read_price(mapple_coin_field))
        print(gold_price_funct.read_price(kruggerand_coin_field))

        print(gold_price_funct.read_price(bar_1_oz_gold_canadein_field))
        print(gold_price_funct.read_price(bar_1_oz_gold_varios_field))

        print(gold_price_funct.read_price(bar_10_oz_gold_varios_field))
        print(gold_price_funct.read_price(bar_10_oz_gold_pamp_suisse_field))

        print(gold_price_funct.read_price(bar_1_kg_gold_canadein_field))

        self.driver.quit() 