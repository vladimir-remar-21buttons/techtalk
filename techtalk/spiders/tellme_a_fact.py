# -*- coding: utf-8 -*-
import scrapy
import random
import xml.etree.ElementTree as ET


class TellMeAFact(scrapy.Spider):

    name = 'tellme_a_fact'
    allowed_domains = ['thefactsite.com']
    start_urls = ['https://www.thefactsite.com/2018/12/1000-interesting-facts.html']
    base_domain = 'https://www.thefactsite.com'

    def parse(self, response):
        
        fatcs_route = '//div[@class="post-content"]//li'
        facts = response.xpath(fatcs_route).extract()
        facts = [''.join(ET.fromstring(e).itertext()) for e in facts]
        
        fact = random.choice(facts)

        yield {'one_fact': fact}