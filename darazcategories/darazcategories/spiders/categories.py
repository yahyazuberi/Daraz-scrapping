import scrapy
from ..items import DarazcategoriesItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'darazcategories'
    start_urls = ['https://www.daraz.pk/']

    def parse(self, response):
        items = DarazcategoriesItem()
        product_categories = response.css('.lzd-site-menu-root-item span::text').extract() 
        product_subcategories = response.css(' li .lzd-site-menu-grand-item span ::text').extract()
        product_categoriesurl = response.css(' li .lzd-site-menu-grand-item a::attr(href)').extract()
        items["product_categories"] = product_categories
        items["product_subcategories"] = product_subcategories
        items["product_categoriesurl"] = product_categoriesurl
        yield items