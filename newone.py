import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/home")
driver.maximize_window()


driver.find_element(By.ID,"session_key").send_keys("ryalini276@gmail.com")
driver.find_element(By.ID,"session_password").send_keys("********")     ////////////password
driver.find_element(By.XPATH,"//button [@type='submit']").click()
driver.find_element(By.CLASS_NAME,"t-16.t-black.t-bold").click()








time.sleep(10)
