from django.shortcuts import render
from django.views import View
from .models import Category, Menu, Drink, Nutrition,Image, Allergy_Drink, Allergy, Size
from django.http import JsonResponse
import json

# Create your views here.

class ProductsView(View):
    def post(self, request):
        
        input_data = json.loads(request.body)
       
        menu = Menu.objects.create(name=input_data["menu"])
        category = Category.objects.create(name=input_data["category"], menu = menu)
        nutrition = Nutrition.objects.create(
            one_serving_kca=input_data["category"], 
            sodium_mg=input_data["category"], 
            saturated_fat_g=input_data["category"], 
            sugars_g=input_data["category"], 
            protein_g=input_data["category"], 
            caffeine_mg=input_data["category"], 
            drink = drink,
            size = size            
            )
        drink = Drink.objects.create(
            korean_name=input_data["category"],
            english_name=input_data["category"],
            description=input_data["category"],            
            category_id = category.id
            )
        image = Image.objects.create(
            image_url=input_data["category"],
            drink_id = drink.id
            )
        allergy_drink = Allergy_Drink.objects.create(
            drink_id = drink.id,
            allergy_id = allergy.id
            )
        allergy = Allergy.objects.create(
            name=input_data["category"]
            )
        size = Size.objects.create(
            name=input_data["category"],
            size_ml=input_data["category"],
            size_fluid_ounce=input_data["category"]            
            )
        
        product.save()

        return JsonResponse({"message" : "SUCCESS"}, status=201})
