from click import password_option
from django.views import View
from .models import User
from django.http import JsonResponse
import json

# Create your views here.
class UserView(View):
    def post(self, request):
        input_data = json.loads(request.body)

        users = User.objects.create(name=input_data["user_name"], email=input_data["owner_email"], password=input_data["user_password"], phone=input_data["user_phone"])
     
        return JsonResponse({"message" : "SUCCESS"}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        result = []
        for owner in owners:
            d =  [
                {"이름":dog.name, "나이":dog.age} for dog in Dog.objects.filter(owner_id=owner.id)
            ]
            result.append({
                "name" : owner.name,
                "email" : owner.email,
                "age" : owner.age,
                "created_at" : owner.created_at,
                "dog_list" : d

        
            })
        return JsonResponse({'owner' : result}, status=200)

# class DogView(View):
#     def post(self, request):
#         input_data = json.loads(request.body)

#         dog = Dog.objects.create(name=input_data["dog_name"], age=input_data["dog_age"], owner_id=input_data["owner_id"])
     
#         return JsonResponse({"message" : "SUCCESS"}, status=201)

#     def get(self, request):
#         dogs = Dog.objects.all()
#         result = []
#         for dog in dogs:
#             o = [
#                 {"주인이름": owner.name}  for owner in Owner.objects.filter(id=dog.owner_id)
#             ]
#             result.append({
#                 "name" : dog.name,
#                 "ownew_name" : o , 
#                 "age" : dog.age,
#                 "created_at" : dog.created_at
#             })
#         return JsonResponse({'dog' : result}, status=200)


