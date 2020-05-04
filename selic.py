import requests, bs4

source = requests.get('https://receita.economia.gov.br/orientacao/tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic').text
selic_soup = bs4.BeautifulSoup(source, 'lxml')
# print(selic_soup.prettify())
table = selic_soup.find('content-core')
print(table)


