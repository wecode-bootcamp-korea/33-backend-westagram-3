import json
import re

from django.http    import JsonResponse
from django.views   import View

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

            if User.objects.filter(mail=mail).exists():
                return JsonResponse({"message": "INVALID_MAIL"}, status=400)
               
            if re.match(REX_MAIL, mail) == None:
                return JsonResponse({"message": "INVALID_MAIL"}, status=400)

            if re.match(REX_PASSWORD, password) == None:
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=400)

            User.objects.create(
                name     = name,
                mail     = mail,
                password = password,
                number   = number,
            )

            return JsonResponse({'Message': 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
                



            
