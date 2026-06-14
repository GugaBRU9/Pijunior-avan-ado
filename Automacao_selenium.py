

from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Abrir o navegador
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.saucedemo.com")

#driver.find_element("id","login_credentials").text

## Acessa os espaços para login e coloca os dados
driver.find_element("id","user-name").send_keys("standard_user")
driver.find_element("id","password").send_keys("secret_sauce")

## Procura o botão do login e clica para passar para a próxima página
driver.find_element("id","login-button").click()



## Procura os botões para adicionar cada item ao carrinho

buttons = driver.find_elements(
    "css selector",
    '[id^="add-to-cart-sauce"]'
)

for button in buttons:
    ## Move a tela até aparecer o botão
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        button
    )
    ## Aguarda 10 segundos até que o botão esteja clicável
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(button)
    )

    button.click()

  
## Abre o carrinho
driver.find_element("class name","shopping_cart_link").click()



## Abre a página de checkout
checkout = driver.find_element("id","checkout")

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkout)

WebDriverWait(driver, 10).until(ec.element_to_be_clickable(checkout))

checkout.click()


## Preenche as informações do checkout

driver.find_element("id","first-name").send_keys("Trainee")
driver.find_element("id","last-name").send_keys("PiJunior")
driver.find_element("id","postal-code").send_keys("31270-901")