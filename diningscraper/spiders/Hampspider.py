import scrapy


class HampSpiderLunch(scrapy.Spider):
    name = "hampspider"
    allowed_domains = ["umassdining.com"]
    start_urls = ["https://umassdining.com/locations-menus/hampshire/menu"]

    def parse(self, response):
        fooddict={}
        for food in response .css('div.dinner_fp li '):
            name=food.css('a::attr(data-dish-name)').get()
            allergens=food.css('a::attr(data-allergens)').get()
            calories=food.css('a::attr(data-calories)').get()
            print('name is',name)
            print('allergens is',allergens)
            print('calories is',calories)

            fooddict[name] = {
                'allergens': allergens,
                'calories': calories
            }
        yield fooddict
       
        