import requests
from bs4 import BeautifulSoup
import csv
import scraper_helper as sh
import json


def get_html(url: str):
    response = requests.get(url)
    return response.text


def extract_data(text: str) -> list:
    soup = BeautifulSoup(text, 'lxml')
    data = []
    for post in soup.find_all('article', class_='blog-post'):
        title_element = post.find('h2', class_='blog-post-title')
        title = title_element.text if title_element else None

        body_element = post.find('div', class_='entry-content')
        body = sh.cleanup(body_element.text) if body_element else None

        publised_element = post.find('time', class_='published')
        published = publised_element.text if publised_element else None

        data.append({
            'title': title,
            'body': body,
            'published': published
        })

    return data


def save_csv(data: list):
    with open('posts.csv', 'w', encoding='utf-8') as file:
        fieldnames = ['title', 'body', 'published']
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        writer.writerows(data)


def save_json(data: list):
    with open('posts.json', 'w') as d:
        json.dump(data, d)


def main():
    url = 'http://scrapebay.com/blog/'
    html = get_html(url)
    data = extract_data(html)
    save_json(data)
    save_csv(data)


if __name__ == '__main__':
    main()
