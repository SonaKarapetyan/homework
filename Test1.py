from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()
assert driver.find_element(By.ID, "hplogo").is_displayed()
driver.find_element(By.XPATH, '//*[@id="tsf"]//div[2]/input').send_keys('2pac')
driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
time.sleep(3)
assert (driver.find_element(By.XPATH, '//*[@id="rso"]/div[2]/div/div[1]/div/div/div[1]/a/h3').text == 'Home - 2PAC')
driver.quit()
