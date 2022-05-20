from django.views import View
from .models import Owner, Dog
from django.http import JsonResponse
import json

# Create your views here.
class OwnerView(View):
    def post(self, request):
        input_data = json.loads(request.body)

        owner = Owner.objects.create(name=input_data["owner_name"], email=input_data["owner_email"], age=input_data["owner_age"])
     
        return JsonResponse({"message" : "SUCCESS"}, status=201)

class DogView(View):
    def post(self, request):
        input_data = json.loads(request.body)

        dog = Dog.objects.create(name=input_data["dog_name"], age=input_data["dog_age"], owner_id=input_data["owner_id"])
     
        return JsonResponse({"message" : "SUCCESS"}, status=201)
