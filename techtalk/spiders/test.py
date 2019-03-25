from scrapy.spiders import XMLFeedSpider
from techtalk.items import TechtalkItem


class Test_xml(XMLFeedSpider):
    name = 'test'
    allowed_domains = ['example.com']
    # start_urls = ['https://productdata.awin.com/datafeed/download/apikey/6cfa760914efead8bf95ff06912b599b/language/es/fid/24923/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,brand_id,keywords,product_short_description,category_name,currency,store_price,merchant_deep_link,language,display_price,large_image,rrp_price,product_price_old,in_stock,stock_status,stock_quantity,Fashion%3Asuitable_for,custom_1/format/xml-tree/compression/zip/adultcontent/1/']
    # start_urls = ['https://www.webgains.com/affiliates/datafeed.html?action=download&campaign=194821&feeds=3283&categories=2269,2476,8651,21722,12172,12173,2478,8110,19917,19916,19919,19922,8801,8802,8118,8808,8124,2394,20385,20383,2411,20351,20353,20366,20362,20364,1555,9454,1563,8578,1866,21157,1620,1673,1679,1681,1621,1623,1627,1622,1649,1669,1670,1653,1654,16995,1702,20101,20104,1726,20044,20064,20076,20065,1707,1708,1734,20173,1736,1777,8721,19969,21667,8722&fields=extended&fieldIds=category_path,category_id,description,deeplink,program_id,product_id,image_url,category_name,product_name,price,last_updated,Colour,in_stock,gender,additional_image_2,additional_image_3,image_url,brand,normal_price&format=xml&zipformat=zip&stripNewlines=0&apikey=b63bb8a74f3ce41392ed297defd1dccf']
    start_urls = ['https://productdata.awin.com/datafeed/download/apikey/6cfa760914efead8bf95ff06912b599b/language/en/fid/19935/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,merchant_id,category_name,category_id,aw_image_url,currency,store_price,delivery_cost,merchant_deep_link,language,last_updated,display_price,data_feed_id,brand_name,brand_id,product_short_description,keywords,commission_group,merchant_product_category_path,merchant_product_second_category,merchant_product_third_category,rrp_price,saving,savings_percent,base_price,base_price_amount,base_price_text,product_price_old,in_stock,stock_quantity,stock_status,large_image,Fashion%3Asuitable_for/format/xml-tree/compression/zip/adultcontent/1/']
    # start_urls = ['file:///home/crawler/Descargas/datafeed_325045.xml']
    itertag = 'product'
    # iterator = 'xml'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = TechtalkItem()
        item['name'] = node.xpath('product_name').xpath('text()').get()
        return item
