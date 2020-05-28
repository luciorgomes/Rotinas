from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from easygui import enterbox
import sys

def google_rfb():
    while True:
        searchstring = enterbox(msg="Qual o termo a pesquisar no site da RFB?",title='Pesquisa receita.economia.gov.br')
        if searchstring is None:  # se clicou 'cancel'
            print("Cancel clicked.")
            sys.exit()
        driver = webdriver.Edge()
        driver.get('https://google.com')
        searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input') # Inspector => Copy Xpath
        searchbox.send_keys(searchstring + ' site:receita.economia.gov.br')
        searchbox.send_keys(Keys.ENTER)

