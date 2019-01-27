# -*- coding: utf-8 -*-
import scrapy
import random


class NextEvents(scrapy.Spider):

    name = 'next_events'
    allowed_domains = ['eventbrite.com',
                        'eventbrite.es',
                        'eventbrite.fr',
                        'eventbrite.ca']
    start_urls = ['https://www.eventbrite.com/d/spain--barcelona/events/']
    base_domain = 'https://www.eventbrite.com'

    def parse(self, response):

        list_events_route = '//div[@class="eds-l-pad-all-1"]\
                            //a[@tabindex="0"]/@href'
        list_events = response.xpath(list_events_route).extract()

        # link = 'https://www.eventbrite.es/e/entradas-louis-the-child-sutton-barcelona-51721978831?aff=ebdssbcitybrowse'
        links = random.sample(list_events, 3)
        for link in links:
            yield response.follow(link, self.parse_event)

    def parse_event(self, response):

        date_route = '//time[@class="listing-hero-date"]/@datetime'
        title_route = '//h1[@class="listing-hero-title"]//text()'
        organizer_route = '//a[@data-d-destination="#listing-organizer"]//text()'    
        price_route = '//div[@class="js-display-price"]//text()'
        artist_route = '//div[@data-automation="artist-list"]//span/a/text()'
        time_event_route = '//div[@class="event-details"]\
                            //div[@class="event-details__data"]\
                            //time[@data-automation="event-details-time"]\
                            //p/text()'
        description_route = '//div[@data-automation="listing-event-description"]//text()'
        image_route = '//meta[@property="og:image"]/@content'

        date = response.xpath(date_route).extract_first()
        title = response.xpath(title_route).extract_first()
        organizer = response.xpath(organizer_route).extract_first()
        price = response.xpath(price_route).extract_first()
        artist = response.xpath(artist_route).extract_first()
        time = response.xpath(time_event_route).extract()
        description = response.xpath(description_route).extract()
        image = response.xpath(image_route).extract_first()

        if time:
            time = [e for e in time if e.strip() != '']
        if price:
            price = price.strip()
        if organizer:
            organizer = organizer.strip()
        if description:
            description = [e for e in description if e.strip() != '']
            description = '\n'.join(description)

        yield {
            'date': date,
            'title': title,
            'organizer': organizer,
            'price': price,
            'artist': artist,
            'time': time,
            'description': description,
            'image': image,
            'link': response.url
        }


