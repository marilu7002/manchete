import requests
from bs4 import BeautifulSoup
url = 'https://tribunademinas.com.br/noticias/economia'
response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    lista_manchetes = []
    main = soup.find ('main')
    r = main.find_all ('div', class_='row')
    coluna = r[1].find ('div', class_='col-sm-8')
    artigos= coluna.find_all('div', class_='row')
    for a in artigos:
            manchete=[]
            h2 = a.find('h2', class_='title')
            if h2:
                manchete.append(h2.text)
            texto = a.find_all('p', class_='excerpt')
            for p in texto:
                manchete.append(p.text)
            lista_manchetes.append(manchete)
    for e in lista_manchetes:
            print (e)
            
else:
    print("Falha na requisição: Status Code", response.status_code)

