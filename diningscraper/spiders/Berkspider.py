import scrapy


class BerkSpiderLunch(scrapy.Spider):
    name = "berkspider"
    allowed_domains = ["umassdining.com"]
    start_urls = ["https://umassdining.com/locations-menus/berkshire/menu"]

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
        # data=response.css('div.lunch_fp li a ').getall()
       
        # # div.lunch_fp li 
        # print('the data is',data)
        # fooddata={}
        # for item in data:
        #     print('item is',item)
        #     print('*******')
            # calorie=item.attrib.get('data-calories')

            
            # name=item.attrib.get('data-dish-name')
            # allergens=item.attrib.get('data-allergens')
            # print('*******cal9rie is',calorie)
        #     yield{
        #         'calorie':calorie
        #     }
        # #     fooddata['calories']=calorie
        #     fooddata['name']=name
        #     fooddata['allergens']=allergens
        # print('finaldictis',fooddata)
        # return fooddata


            # yield{
                        
            #     'calorie':calorie,
            #     'name':name,
            #     'allergens':allergens
            #     }
            # print('thw iten is',item.css('a').attrib['data-healthfulness'])
        #     print('thw iten is',item.css('a'))
        # foods=response.css('div.lunch_fp li a::attr(data-cholestrol)').getall()
        # allergens=response.css('div.lunch_fp li a::attr(data-allergens)').getall()
        # names=response.css('div.lunch_fp li a::attr(data-dish-name)').getall()
        # calories =response.css('div.lunch_fp li a::attr(data-calories)').getall()
        # foodinfo={
        #     'NAME':{'allergens':,'calories':}
        # }
        # for food in allergens:
            
        #     foodinfo['']
          
        # for name in names:
        #     foodinfo[name]=name
        # for calorie in calories:
        #     print(calorie)
        # dinnerfoods=response.css('div.dinner_fp li a::text').getall()
        # healthfulnes=response.css('div.dinner_fp li a::attr(data-healthfulness)').getall()
    
        # print('foods is',foods)
        # print(foods[0])
   
        # print('allhtml is',alhtml)
        
        # for food in foods:
            
        #     yield{
        #         'food_names':food
                
        #         }
        # for dinnerfood in dinnerfoods:
        #     yield{
        #         'dinner_food: ':dinnerfood
        #     }
        