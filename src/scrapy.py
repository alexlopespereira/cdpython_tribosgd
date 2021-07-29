from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.util import wait_element


def get_pagina(driver_next):
    lista_a = driver_next.find_elements_by_xpath('//article/h3/a')
    urls = [a.get_attribute('href') for a in lista_a]
    driver_pagina = webdriver.Chrome(ChromeDriverManager().install())
    resultados = []
    for url in urls:
        driver_pagina.get(url)
        for i in range(3):
            esperar = wait_element(driver_pagina, '//div[@class="col-sm-6 product_main"]', by=By.XPATH)
            if not esperar:
                print(f"Não pegou a página {url}")
                sleep(10)
            else:
                break
        ret = driver_pagina.find_element_by_xpath('//div[@class="col-sm-6 product_main"]')
        titulo = ret.find_element_by_xpath('./h1').text
        preco = float(ret.find_element_by_xpath('./p[1]').text[1:])
        estoque = int(ret.find_element_by_xpath('./p[2]').text.split("(")[1].split(' ')[0])
        descricao = driver_pagina.find_element_by_xpath('//article/p').text
        resultados.append({"titulo": titulo, "preco": preco, "estoque": estoque, "descricao": descricao})

    driver_pagina.close()
    return resultados

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'http://books.toscrape.com/index.html'
driver.get(url)

to_continue = True
dataset = []
while to_continue:
    result = get_pagina(driver)
    dataset.extend(result)
    esperar = wait_element(driver=driver, by_content='//li[@class="next"]/a', by=By.XPATH)
    if esperar:
        bnext = driver.find_element_by_xpath('//li[@class="next"]/a')
        bnext.click()
    else:
        break
    esperar = wait_element(driver=driver, by_content='//li[@class="next"]/a', by=By.XPATH, timeout=15)
    if not esperar:
        to_continue = False


print(dataset)
