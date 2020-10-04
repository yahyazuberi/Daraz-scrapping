import scrapy
from scrapy import Request
from ..items import DarazscriptsItem
import pickle
import json
import pandas as pd

class DarazallSpider(scrapy.Spider):
    name = 'darazscripts'
    rotate_user_agent = True
    API = "24b758ff7772c102f7317b6c2cf0a622"
    categories = []
    # open file and read the content in a list
    with open('F:/Darazdata/darazscripts/listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            categories.append(currentPlace)
    allowed_domains = ['www.daraz.pk']
    start_urls = categories[4500:5000]
    num = 4500
    def parse(self, response):
        items = DarazscriptsItem()
        script = response.css('script::text').extract()
        print(DarazallSpider.num)
        filename = "F:/Darazdata/darazscripts/Categoriesdata/"+str(DarazallSpider.num)
        outF = open(filename, 'w', encoding='utf-8')
        DarazallSpider.num+=1
        for line in (script):
            outF.write(line)
        outF.close()
        DarazallSpider.script_to_dataframe(filename,str(DarazallSpider.num-1))
    
    def script_to_dataframe(filename,num):
        f = open( filename,encoding="utf8")
        data = f.read()
        page = data.find('"page"',500)
        pageno = data[page+8]
        cat = data.find('"value"',50)
        val = data.find("title",cat)
        category = (data[cat+9:val-3])
        dt = data.split('listItems')
        dt2= dt[1].split("breadcrumb")
        dt2[0] = dt2[0][2:]
        dt2[0] = dt2[0][:-2]
        obj = json.loads(dt2[0])
        df= pd.DataFrame(obj)
        df["Pageno"] = pageno
        df["Category"] = category
        pickle.dump( df, open( "F:/Darazdata/darazscripts/Finaldata/"+num, "wb" ) )
    