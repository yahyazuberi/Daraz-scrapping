import scrapy
from scrapy import Request
from ..items import DarazscriptsItem
import pickle
class DarazallSpider(scrapy.Spider):
    name = 'darazscripts'
    categories = pickle.load( open( "F:/Darazdata/darazcategories/darazcategories/categoriesurl+name.pickle", "rb" ) )
    categoriesname = list(categories.keys())
    categoriesurls = list(categories.values())
    allowed_domains = ['www.daraz.pk']
    start_urls = categoriesurls[:10]
    print(start_urls)
    num = 0
    def parse(self, response):
        items = DarazscriptsItem()
        script = response.css('script::text').extract()
        print(DarazallSpider.num)
        outF = open("F:/Darazdata/darazscripts/Categoriesdata/"+str(DarazallSpider.num), 'w', encoding='utf-8')
        DarazallSpider.num+=1
        for line in (script):
        # write line to output file.
            outF.write(line)
        outF.close()