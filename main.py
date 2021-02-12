#pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://github.com/")

print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("IHergueta")
search.send_keys(Keys.RETURN)

user = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/nav[1]/a[10]")
user.send_keys(Keys.RETURN)




time.sleep(5)
driver.close()