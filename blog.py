import scrapy
import scraper_helper as sh

class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_urls = ['http://scrapebay.com/blog']

    def parse(self, response):
        for post in response.css('.blog-post'):
            title = post.css('.blog-post-title ::text').get()

            body_tags = post.css('.entry-content ::text').getall()
            body = ''.join(body_tags)
            body = sh.cleanup(body)

            published = post.css('.published ::text').get()
            
            yield {
                'title': title,
                'body': body,
                'published': published
            }
            
