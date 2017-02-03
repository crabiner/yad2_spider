# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Yad2SpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    SaleDay = Field()
    Address = Field()
    Type = Field()
    Rooms = Field()
    Floor = Field()
    BuildYear = Field()
    Area = Field()
    PartSold = Field()
    Price = Field()