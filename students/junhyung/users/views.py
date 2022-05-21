import json, re, bcrypt, jwt

from django.http    import JsonResponse
from django.views   import View
from django.conf    import settings
from users.models   import User



class SignUpView(View):
    def post(self, request):
        try:

            data = json.loads(request.body)

            name         = data['name']
            mail         = data['mail']
            password     = data['password']
            number       = data['number']
            REX_MAIL     = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            REX_PASSWORD = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"

            hashed_password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8')


            if User.objects.filter(mail=mail).exists():
                return JsonResponse({"Message": "INVALID_MAIL"}, status=400)
               
            if not re.match(REX_MAIL, mail):
                return JsonResponse({"Message": "INVALID_MAIL"}, status=400)

            if not re.match(REX_PASSWORD, password):
                return JsonResponse({"Message": "INVALID_PASSWORD"}, status=400)

            User.objects.create(
                name     = name,
                mail     = mail,
                password = hashed_password,
                number   = number,
            )

            return JsonResponse({'Message': 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'Message': 'KEY_ERROR'}, status=400)
                

class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            mail     = data['mail']
            password = data['password']
            user     = User.objects.get(mail = mail)

            # if not User.objects.filter(mail = mail).exists():
            #     return JsonResponse({'Message' : 'INVALID_USER' }, status=401)

            if not bcrypt.checkpw(password.encode('UTF-8'), user.password.encode('UTF-8')):
                return JsonResponse({'Message' : 'INVALID_PASSWORD'}, status=401)

            token = jwt.encode({'user_id':user.id}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
            return JsonResponse({'token' : token}, status=200)


        except KeyError:
            return JsonResponse({'Message' : 'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'Message' : 'INVALID_USER'}, status=401)

            
