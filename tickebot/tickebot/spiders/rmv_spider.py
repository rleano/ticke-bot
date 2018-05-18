import scrapy


class QuotesSpider(scrapy.Spider):
    name = "license"
    start_urls = [
        'https://www.dmv.org/ma-massachusetts/apply-license.php',
    ]

    # def start_requests(self):
    #     urls = [
    #         'https://www.dmv.org/ma-massachusetts/apply-license.php',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result = []
        # requirement_list = response.xpath('//*[@id="content1"]/ul[1]')
        # requirement_list = response.css('#content1 > ul:nth-child(9)')
        items = response.css('#content1 > ul:nth-child(9) > li')
        self.log('ITEMS: %d' % len(items))
        for item in items:
            item_textlist = item.css("::text").extract()
            item_text = ''.join(item_textlist)
            self.log('TEXT: %s' % item_text)
            result.append(item_text)
        filename = 'rmv.txt'

        for line in result:
            self.log('LINE: %s' % line)
        with open(filename, 'w') as f:
            for line in result:
                f.write("%s\n" % line)

        self.log('Saved file %s' % filename)
