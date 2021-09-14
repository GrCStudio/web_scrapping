import requests
from bs4 import BeautifulSoup

# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
# Ваш код


def habr_full_scrapping():
    # получаем страницу с самыми свежими постами
    page_response = requests.get('https://habr.com/ru/all/')
    page_response.raise_for_status()

    soup = BeautifulSoup(page_response.text, 'html.parser')

    # извлекаем посты
    articles = soup.find_all('article')

    habr_link = 'https://habr.com'
    for article in articles:
        title = article.find('h2')
        ar_name = title.find('span').text
        ar_href = title.find('a').attrs.get('href')
        ar_date = article.find('time').attrs.get('title')
        ar_response = requests.get('https://habr.com' + ar_href)
        ar_soup = BeautifulSoup(ar_response.text, 'html.parser')
        article = ar_soup.find('article')
        for tag in KEYWORDS:
            if tag in article.text:
                print(f'Дата: {ar_date} - Заголовок: {ar_name} - Ссылка: {habr_link + ar_href}')
                