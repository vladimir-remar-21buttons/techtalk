# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TechtalkItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    reference = scrapy.Field()
    price = scrapy.Field()
    original_price = scrapy.Field()
    price_amount = scrapy.Field()
    price_currency = scrapy.Field()
    sizes = scrapy.Field()
    colors = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image = scrapy.Field()
    image_thumb = scrapy.Field()
    image_smedium = scrapy.Field()
    image_height = scrapy.Field()

    title1 = scrapy.Field()
    title2 = scrapy.Field()
    title3 = scrapy.Field()
    pass
