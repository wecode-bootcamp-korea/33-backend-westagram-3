# from django.shortcuts import render

# Create your views here.
import json
import re
import bcrypt 
import jwt

from django.http import JsonResponse
from django.views import View

from .models import User
from my_settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            input_data = json.loads(request.body)
            email = input_data['email']
            password = input_data['password']

            # 기존에 존재하는 이메일이 중복되면 중복 에러 메세지 반환
            if User.objects.filter(email = email).exists():
                return JsonResponse({"message" : "THE_USER_EMAIL_ALREADY_EXISTS"}, status=400)
            # 이메일에 @ 또는 .이 없으면 에러 반환 
            if not re.match(r"^[a-zA-Z0-9+-_.]+@/[a-zA-Z0-9-.]+\.[a-zA-Z0-9-]$", email):
                return JsonResponse({"message" : "INVALID_EMAIL_--_NEEDS_@_AND_."}, status=400)
            # 비밀번호는 8자리 이상, 문자 숫자, 특수문자의 복합 -- 그러지 않을 경우, 에러 반환
            if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", password):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8")

            User.objects.create(
                name          = input_data['name'],
                email         = email,
                password      = hashed_password,
                mobile_number = input_data['mobile_number'],
            )
            return JsonResponse({"messsage" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KeyError"}, status=400)
    
class SignInView(View):
    def post(self,request):
        try:
            input_data = json.loads(request.body)

            # non-existent log-in info & wrong password
            if not User.objects.filter(email = input_data['email'], password = input_data['password']).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status=401)
            
            if bcrypt.checkpw(input_data['password'].encode('UTF-8'), input_data['password'].encode('UTF-8')):
                user = User.objects.get(email = input_data['email'])
                token = jwt.encode({'user' : user.id}, SECRET_KEY, algorithm='HS256').decode('UTF-8')
                return JsonResponse({"token" : token}, status=200)

            # log-in success
            # return JsonResponse({"message" : "SUCCESS"}, status=200)

            # account/password not delievered
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)