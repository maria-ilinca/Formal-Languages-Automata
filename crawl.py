from bs4 import BeautifulSoup
import sys
import requests
import re
import lxml


def getHTMLdocument(url):
    response = requests.get(url)
    return response.text


url_to_scrape = "https://www.olx.ro/locuri-de-munca/"  # url initial din care putem sa cream paginile
urls_on_pages = [url_to_scrape]  # lista cu url-ul fiecarei pagini
for i in range(25):
    urls_on_pages.append(url_to_scrape + f"?page={i}")

print(urls_on_pages)


# for i in range(len(urls_on_pages)):
def htmlToSoup(link):
    print(link)
    html_document = getHTMLdocument(link)  # documentul html ca string
    # print(html_document)
    soup = BeautifulSoup(html_document, 'lxml')  # fisierul html ca soup
    # print(soup.prettify())
    return soup


lsLink = []  # contine toate linkurile care duc spre pagina proprie a unui anunt pentru a putea parsa descrierea
x=0
for url in urls_on_pages:
    soup = htmlToSoup(url)
    contine_link = soup.find_all('div',
                                 class_='space rel')  # o parte din html care contine linkul catre pagina anuntului
    # print(contine_link)
    for element in contine_link:
        newSoup = element
        link = newSoup.find_all('a')
        # print(type(link))
        for el in link:
            lsLink.append(el.get('href'))

lista_descriere = []  # titlul plus descrierea pentru fiecare anunt
for linkDescriere in lsLink:
    soup = htmlToSoup(linkDescriere)
    # lista_descriere.append(soup)
    descriere = str(soup.find('div', class_='css-2t3g1w-Text'))
    titlu = str(soup.find('h1', class_='css-r9zjja-Text eu5v0x0'))
    lista_descriere.append((titlu, descriere))
inf = open("info.txt", 'w', encoding="utf-8")
for element in lista_descriere:
    inf.write(element[0])
    inf.write('\n')
    inf.write(element[1])
    inf.write('\n')
inf.close()
# print(lista_descriere)







