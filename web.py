import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME,"email").send_keys("yaliniragu@outlook.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Yazini2708@")

# XPATH-----------//tagname[@attribute='value']--->  //input [@class='form-control ng-untouched ng-pristine ng-invalid']
#     CSS--------------------- //tagname[@attribute='value']   ,#id  ,.classname
driver.find_element(By.XPATH,"//input [@class='form-control ng-untouched ng-pristine ng-invalid']").send_keys("YALINI R")

driver.find_element(By.ID,"exampleCheck1").lick()

driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

driver.find_element(By.XPATH,"//input [@class='btn btn-success']").click()

# gender=

msg=driver.find_element(By.CLASS_NAME,"alert-success").text
print(msg)

assert "Success" in msg










time.sleep(10)