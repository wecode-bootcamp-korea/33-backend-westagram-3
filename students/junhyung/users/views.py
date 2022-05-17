# from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views import View

from users.models import User
import re

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)


            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "ERROR_EMAIL_ALREADY_EXIST"}, status=400)
               
            if (data["email"] == "") or (data["password"] == ""):
                return JsonResponse({"message": "ERROR_EMPTY_EMAIL_OR_PASSWORD"}, status=400)
               
            if re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data["email"]) == None:
                return JsonResponse({"message": "ERROR_EMAIL_NEED_@AND."}, status=400)

            if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", data["password"]) == None:
                return JsonResponse({"message": "ERROR_REQUIRE_8_LETTER,NUMBER,SPECIAL_SYMBOLS)"}, status=400)
               
            return JsonResponse({'Message': 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
                



            name = data['name']
            mail = data['mail']
            password = data['password']
            number = data['number']


            email_regex = "'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'"
            password_regex = ""