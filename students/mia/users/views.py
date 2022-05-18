# Create your views here.

import json
import re
import bcrypt 
import jwt

from django.http  import JsonResponse
from django.views import View
from django.conf  import settings

from .models      import User

class SignUpView(View):
    def post(self, request): 
        try: 
            input_data = json.loads(request.body)
            email      = input_data['email']
            password   = input_data['password']
          
            if User.objects.filter(email = email).exists():
                return JsonResponse({"message" : "THE_USER_EMAIL_ALREADY_EXISTS"}, status=400)

            if not re.match(r"^[a-zA-Z0-9+-_.]+@/[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                return JsonResponse({"message" : "INVALID_EMAIL_--_NEEDS_@_AND_."}, status=400)
         
            if not re.match(r"^(?=.{8,16}$)(?=.*[a-z])(?=.*[0-9]).*$", password):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8")

            User.objects.create(
                name          = ['name'],
                email         = email,
                password      = hashed_password,
                mobile_number = ['mobile_number']
            )
            return JsonResponse({"messsage" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KeyError"}, status=400)
    
class SignInView(View):
    def post(self,request):
        try:
            
            input_data = json.loads(request.body)

            email    = input_data['email']
            password = input_data['password']
            user  = User.objects.get(email = email)

            if not User.objects.filter(email = email).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status=401)

            if bcrypt.checkpw(password.encode('UTF-8'), user.password.encode('UTF-8)')):
                token = jwt.encode({'user' : user.id}, settings.SECRET_KEY, settings.ALGORITHM)
                return JsonResponse({'token' : token}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        