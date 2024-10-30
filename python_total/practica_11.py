import requests
import bs4

url = 'https://books.toscrape.com/'
result = requests.get(url)
print(type(result.text))

soup = bs4.BeautifulSoup(result.text, 'lxml')
print()
print(type(soup))
print()
print(soup.select('title')[0].getText())


# Extraer elementos

print()
print(soup.select('form')[0:2])  # Buscador de etiquetas
print()
print(soup.select('.image_container')[0:2])  # Buscador de clases
print()
for i in soup.select('.image_container img')[0:3]:  # Buscador de elementos dentro de otros elementos
    print(i)
print()
print(soup.select('.image_container>img')[0:3])
print()
for i in soup.select('.image_container>a')[0:3]:  # Buscador de elementos directos dentro de otros elementos
    print(i)

# Extraer imágenes
print()
print('   *** Imagenes ***')
print()
for i in soup.select('img'):
    print(url + i.get('src'))



