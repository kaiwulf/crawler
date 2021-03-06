import urllib3, re
from bs4 import BeautifulSoup
from csv import DictReader, DictWriter

# https://css-tricks.com/snippets/css/a-guide-to-flexbox/
# Using sample program from below to learn more about python webscrapping
# https://dzone.com/articles/webscraping-with-python-beautiful-soup-and-urllib3

class search:

    def __init__(url=None, key_words=None):
        self.url = url
        self.key_words = key_words


class crawler:

    def __init__():
        pass

def get_book_data(filename):
    titles = []
    prices = []
def gdb_to_usd(amount):
    return f's {round(amount * 1.21255), 2}'

for i in range(1,51):
    url = f'http://books.toscrape.com/catalogue/category/books_1/page-{i}.html'
    req = urllib3.PoolManager()
    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')
    contents = soup.find_all(class_='product_pod')
    input(type(soup.find_all()))
    titles = []
    for j in soup.find_all():
        titles.append(j['title'])
    pounds = []
    c = []
    for i in contents:
        c.append(i.find().get_text())
        for number in c:
            amount = re.compile('[0-9]+.')
            num = amount.findall(number)
            pounds.append(float(''.join(num)))
    temp = list(map(gdp_to_usd_rounded,pounds))
    for t in temp:
        prices.append(t)

    res = dict(zip(titles,prices))


    if 'title' in i.attrs:
        input("title in attrs")
        titles.append(i['title'])
    pounds = []
    c = []