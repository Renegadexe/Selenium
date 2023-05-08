from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import data
import time


path = "chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)

driver.get("https://comparatif-tarifs-bancaires.ma/fr/page/comparatif_bancaire")

time.sleep(5)

for choice in data.drop_1_options:
    _1 = driver.find_element(By.XPATH, data.drop_1).click()
    _2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, choice))).click()
    _3 = driver.find_element(By.XPATH, data.drop_2).click()
    _4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data.drop_2_options))).click()
    _5 = driver.find_element(By.XPATH, data.drop_3).click()
    for option in data.drop_3_options [:4]:
        _6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, option))).click()
    _7 = driver.find_element(By.XPATH, data.drop_4).click()
    _8 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data.drop_4_options[0]))).click()
    _9 = driver.find_element(By.XPATH, data.submit).click()





    




#driver.back()
#driver.refresh()