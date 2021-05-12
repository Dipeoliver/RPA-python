from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time
import pyperclip


# driver = webdriver.Ie(r"C:\Users\diego.oliveira.LGE\AppData\Local\Programs\Python\Python39\IEDriverServer.exe")
driver = webdriver.Chrome()

driver.get("https://www.uol.com.br//")

casa = driver.find_element_by_by_xpath('/html/body/header/div[2]/div/div[3]/div/div/input').send_keys("bolsonaro")
print(casa)
# driver.get("https://dolarhoje.com/")
# # cotacao_dolar = driver.find_element_by_xpath('//*[@id="nacional"]').get_attribute("value")
# print(teste)
