from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

#SWP
button_display_field = (By.XPATH, "//button[@class='btn btn-default dropdown-toggle']")
button_24_display_field = (By.XPATH, "//a[normalize-space()='24']")

gold_price_field = (By.XPATH, "/html/body/logo-feed/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]")
silver_price_field = (By.CSS_SELECTOR, "tbody tr:nth-child(2) td:nth-child(2)")

mapple_coin_field = (By.CSS_SELECTOR, "body > pages-products:nth-child(25) > div:nth-child(11) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > small:nth-child(1) > strong:nth-child(2)")
kruggerand_coin_field = (By.CSS_SELECTOR, "body > pages-products:nth-child(25) > div:nth-child(11) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > small:nth-child(1) > strong:nth-child(2)")

bar_1_oz_gold_canadein_field = (By.CSS_SELECTOR, "body > pages-products:nth-child(25) > div:nth-child(11) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > small:nth-child(1) > strong:nth-child(2)")
bar_1_oz_gold_varios_field = (By.CSS_SELECTOR, "body > pages-products:nth-child(25) > div:nth-child(11) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > small:nth-child(1) > strong:nth-child(2)")

bar_10_oz_gold_pamp_suisse_field = (By.CSS_SELECTOR, "body > pages-products:nth-child(25) > div:nth-child(11) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(16) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > small:nth-child(1) > strong:nth-child(2)")
bar_10_oz_gold_varios_field = (By.CSS_SELECTOR, "body > pages-products:nth-child(25) > div:nth-child(11) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(15) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > small:nth-child(1) > strong:nth-child(2)")

bar_1_kg_gold_canadein_field = (By.CSS_SELECTOR, "body > pages-products:nth-child(25) > div:nth-child(11) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(20) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > small:nth-child(1) > strong:nth-child(2)")
