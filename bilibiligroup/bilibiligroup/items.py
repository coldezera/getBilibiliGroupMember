# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class BilibiligroupItem(scrapy.Item):
    # define the fields for your item here like:
    user_url = Field()
    PrivateProfile = Field()
    CSGO = Field()
    VACBan = Field()
    GameBan = Field()
    pass
