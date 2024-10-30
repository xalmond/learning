import requests
import bs4
import re


def generate_page_source():
    page = 0
    while page >= 0:
        page += 1
        url = f'https://books.toscrape.com/catalogue/page-{str(page)}.html'
        yield page, requests.get(url)


# Init variables
page_source = generate_page_source()
page_exists = True

# Iter every page in book shop
while page_exists:
    page, source = next(page_source)
    # Page not found
    if source.status_code != 200:
        page_exists = False
    else:
        soup = bs4.BeautifulSoup(source.text, 'lxml')
        # Every book is in class=product_pod
        for book in soup.select('.product_pod'):
            for rating, rating_num in [['Four', 4], ['Five', 5]]:
                # Rating is in class=stsr-rating xxx
                if len(book.select(f'.star-rating.{rating}')) >= 1:  # ' ' a '.'
                    # Book title is in tag title
                    print(str(page).zfill(2) +\
                          ' - ' + '*' * rating_num + ' ' * (5 - rating_num) + ' - ' +\
                          book.select('h3 a')[0]['title'])









