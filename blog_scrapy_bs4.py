import scrapy
from bs4 import BeautifulSoup
import scraper_helper as sh

class BlogBS4Spider(scrapy.Spider):
    name = 'blog_bs4'
    start_urls = ['http://scrapebay.com/blog']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        for post in soup.find_all('article', class_='blog-post'):
            title_element = post.find('h2', class_='blog-post-title')
            title = title_element.text if title_element else None

            body_element = post.find('div', class_='entry-content')
            body = sh.cleanup(body_element.text) if body_element else None

            publised_element = post.find('time', class_='published')
            published = publised_element.text if publised_element else None

            yield {
                'title': title,
                'body': body,
                'published': published
            }
            


