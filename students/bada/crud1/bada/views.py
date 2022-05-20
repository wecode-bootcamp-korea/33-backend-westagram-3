
from django.views import View
from .models import Category, Menu, Drink, Nutrition,Image, Allergy_Drink, Allergy, Size
from django.http import JsonResponse
import json

# Create your views here.

class MenuView(View):
    def post(self, request):
        input_data = json.loads(request.body)
        """
        {
            menu_name  : "콜드브루",
        }
        """
        menu = Menu.objects.create(name=input_data["menu_name"])

        return JsonResponse({"message" : "SUCCESS"}, status=201)

    def get(self, request):
        menus = Menu.objects.all()
        result = []
        for menu in menus:
            result.append({
                "id" : menu.id,
                "name" : menu.name,
                "create_at" : menu.created_at
            })
    
        return JsonResponse({'menu' : result}, status=200)
        # def get(self, request):
        #     menu = Menu.objects.all()
        #     result = [{"name" : menu.name}]
        #     # for menu in menus:
        #     #     result.append({
        #     #         "id" : menu.id,
        #     #         "name" : menu.name,
        #     #         "create_at" : menu.created_at
        #     #     })
        #     # for menu in menus:
        #     #     result.append({"name" : menu.name})
        
        #     return JsonResponse({'menu' : result}, status=200)




#     def get(self, request):
# #상품 목록을 반환해준다. 
# 	    result = []  # 리스트를 먼저 만들어 놓는다. 

# 	    # 모든 상품 목록을 가져오려면
# 	    menus = Menu.objects.all()
#         for menu in menus:
#             result.append({"name" : menu.name})
	
#         return JsonResponse({"menu" : result}, status=200)

# class ProductsView(View):
#     def post(self, request):
        
#         input_data = json.loads(request.body)
#         """
#         {
#             menu  : "콜드브루",
#             korean_name : '바닐라 플랫 화이트',
#             english_name : 'vailla', 
#             description :'맛있어 보인다.', 
#             category_id : 2
#         }
#         """
       
        

#         category = Category.objects.create(name=input_data["category"], menu = menu)
#         nutrition = Nutrition.objects.create(
#             one_serving_kca = input_data["category"], 
#             sodium_mg = input_data["category"], 
#             saturated_fat_g=input_data["category"], 
#             sugars_g=input_data["category"], 
#             protein_g=input_data["category"], 
#             caffeine_mg=input_data["category"], 
#             drink = drink,
#             size = size            
#             )

#         # Case 1
#         drink = Drink.objects.create(
#             korean_name=input_data["category"],
#             english_name=input_data["category"],
#             description=input_data["category"],            
#             category_id = category.id
#             )

#         # Case 2
#         drink = Drink(
#             korean_name=input_data["category"],
#             english_name=input_data["category"],
#             description=input_data["category"],            
#             category_id = category.id
#         )
#         drink.save()

        

#         image = Image.objects.create(
#             image_url=input_data["category"],
#             drink_id = drink.id
#             )
#         allergy_drink = Allergy_Drink.objects.create(
#             drink_id = drink.id,
#             allergy_id = allergy.id
#             )
#         allergy = Allergy.objects.create(
#             name=input_data["category"]
#             )
#         size = Size.objects.create(
#             name=input_data["category"],
#             size_ml=input_data["category"],
#             size_fluid_ounce=input_data["category"]            
#             )
        
#         # product.save()

#         return JsonResponse({"message" : "SUCCESS"}, status=201)
