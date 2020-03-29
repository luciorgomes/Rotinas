import random
import selenium
from selenium.webdriver.common.keys import Keys

def run_2048():
    browser = selenium.webdriver.Firefox()
    browser.get('https://play2048.co/')
    htmlElem = browser.find_element_by_tag_name('html')
    while True:
        for i in range(600):
            key = random.randint(1, 4)
            if key == 1:
                htmlElem.send_keys(Keys.DOWN)
            elif key == 2:
                htmlElem.send_keys(Keys.UP)
            elif key == 3:
                htmlElem.send_keys(Keys.LEFT)
            else:
                htmlElem.send_keys(Keys.RIGHT)
            print(key)

        linkElem = browser.find_element_by_link_text("Try again")
        linkElem.click()

if __name__ == '__main__': # executa se chamado diretamente
    run_2048()