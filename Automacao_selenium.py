

from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

# Abrir o navegador
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

## Função para procurar e clicar nos botões da página
def button_search(button):
    ## Verifica a localização do botão na página
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        button
    )
    ## Aguarda 10 segundos até o botão ser pressionavel
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(button)
    )
    ## Clica o botão especificado
    button.click()

## Acessa o site saucedemo
driver.get("https://www.saucedemo.com")

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
    button_search(button)

  
## Abre o carrinho
driver.find_element("class name","shopping_cart_link").click()



## Abre a página de checkout
checkout = driver.find_element("id","checkout")

button_search(checkout)


## Preenche as informações do checkout

driver.find_element("id","first-name").send_keys("Trainee")
driver.find_element("id","last-name").send_keys("PiJunior")
driver.find_element("id","postal-code").send_keys("31270-901")


## Clicando no botão de continuar a compra
button_continue = driver.find_element("id","continue")
button_search(button_continue)

## Raspando informações da compra em uma lista, primeiro valor se refere ao meio de pagamento e o segundo a forma de entrega
lista=driver.find_elements("class name","summary_value_label")

## Mostra o meio de pagamento
print(lista[0].text)

## Mostra a forma de entrega
print(lista[1].text)

## Obtem o valor total da compra
quantia_total=driver.find_element("class name","summary_total_label").text

## Clicar no botão finish

button_finish = driver.find_element("id","finish")
button_search(button_finish)

## Obtem a mensagem de confirmação da compra
mensagem_conf=driver.find_element("class name","complete-text").text
