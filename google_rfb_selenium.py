import sys

from easygui import enterbox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def google_rfb():
    while True:
        searchstring = enterbox(msg="Qual o termo a pesquisar no site da RFB?",title='Pesquisa receita.economia.gov.br')
        if searchstring is None:  # se clicou 'cancel'
            print("Cancel clicked.")
            sys.exit()
        driver = webdriver.Chrome()
        driver.get('https://google.com')
        searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input') # Inspector => Copy Xpath
        searchbox.send_keys(searchstring + ' site:receita.economia.gov.br')
        searchbox.send_keys(Keys.ENTER)

if __name__ == '__main__': # executa se chamado diretamente
    google_rfb()