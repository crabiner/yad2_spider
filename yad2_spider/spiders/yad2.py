# -*- coding: utf-8 -*-
import scrapy
from yad2_spider.items import Yad2SpiderItem


class Yad2Spider(scrapy.Spider):
    name = "yad2"
    allowed_domains = ["homeprices.yad2.co.il/street/%D7%9B%D7%A4%D7%A8-%D7%A1%D7%91%D7%90/%D7%A9%D7%9C%D7%9E%D7%94-%D7%95%D7%97%D7%99%D7%94-%D7%90%D7%A0%D7%92%D7%9C-38"]
    start_urls = ['http://homeprices.yad2.co.il/street/%D7%9B%D7%A4%D7%A8-%D7%A1%D7%91%D7%90/%D7%A9%D7%9C%D7%9E%D7%94-%D7%95%D7%97%D7%99%D7%94-%D7%90%D7%A0%D7%92%D7%9C-38/']

    def parse(self, response):
        #table = response.xpath('//*[ @ id = "td_area_con"]')
        #rows = table.xpath('./table/tbody/tr')
        rows = response.xpath('//*[ @ id = "td_area_con"]/table/tr')
        print len(rows)
        num_rows = len(rows)
        count = 0
        for row in rows:
            count = count+1
            if (count == 1):
                continue
            if (count == (num_rows - 1)):
                break
            item = Yad2SpiderItem()
            item['SaleDay'] = row.xpath('./td[1]/a/div/text()').extract_first()
            item['Address'] = row.xpath('./td[2]/a/div/text()').extract_first()
            item['Type'] = row.xpath('./td[3]/a/div/text()').extract_first()
            item['Rooms'] = row.xpath('./td[4]/a/div/text()').extract_first()
            item['Floor'] = row.xpath('./td[5]/a/div/text()').extract_first()
            item['BuildYear'] = row.xpath('./td[6]/a/div/text()').extract_first()
            item['Area'] = row.xpath('./td[7]/a/div/text()').extract_first()
            item['PartSold'] = row.xpath('./td[8]/a/div/text()').extract_first()
            item['Price'] = row.xpath('./td[9]/a/div/text()').extract_first()
            yield {
                'SaleDay' : item['SaleDay'].strip(),
                'Address': item['Address'].strip(),
                'Type': item['Type'].strip(),
                'Rooms': item['Rooms'].strip(),
                'Floor': item['Floor'].strip(),
                'BuildYear': item['BuildYear'].strip(),
                'Area': item['Area'].strip(),
                'PartSold': item['PartSold'].strip(),
                'Price': item['Price'].strip(),
            }