import scrapy
i = 1
thislist = []
temp = 1
class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    
    f = open("linkspy.txt", "r")
    for x in f:
        thislist.append(x)
        print(x)
    start_urls = [thislist[0]]
    #i = 1
    def parse(self, response):
        global thislist 
        global i 
        global temp
        categories = ""
        link = "https://daringboy.com/?s="
        SET_SELECTOR = '.post-link'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::attr(title)'
            #PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            #MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            
            if temp == 1: 
                categories = str(thislist[i-1].replace(link,"").replace("+"," ")) 
            else: 
                categories = ""
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'category': categories,
                'name': str(brickset.css(NAME_SELECTOR).extract_first()).replace(",",""),
                #'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                #'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': str(brickset.css(IMAGE_SELECTOR).extract_first()).replace("-500x500",""),
            }
            temp += 1
        NEXT_PAGE_SELECTOR = '.next ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            print("next page")
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
        elif i < len(thislist):
            print("next link")
            i = i + 1
            temp = 1
            yield scrapy.Request(
                response.urljoin(thislist[i-1]),
                callback=self.parse
            )