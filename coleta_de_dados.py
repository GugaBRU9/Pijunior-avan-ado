import pandas

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"

driver = webdriver.Firefox()
driver.get(url)

senha = "secret_sauce"
username = "standard_user"

elem_username = driver.find_element(By.ID, "user-name")
elem_senha = driver.find_element(By.ID, "password")

elem_senha.send_keys(senha)
elem_username.send_keys(username)

elem_login = driver.find_element(By.ID, "login-button")
elem_login.click()

dicionario = {"nome":[], "descricao":[], "preco":[]}

descs = driver.find_elements(By.CLASS_NAME, "inventory_item_desc")
precos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
nomes = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

for d in descs:
    dicionario["descricao"].append(d.text)

for p in precos:
    dicionario["preco"].append(p.text)

for n in nomes:
    dicionario["nome"].append(n.text)
