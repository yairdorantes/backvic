from django.views import View
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import IntegrityError
# Create your views here.
from .models import Paciente
from django.contrib.auth import authenticate

class Login(View):
    def get(self, request):
        return JsonResponse({"mensaje":"exito"})
    def post(self, request):
        datos = json.loads(request.body)
        email = datos["email"]
        contrasena = datos["contrasena"]
        usuario = authenticate(username=email,password=contrasena)
        if usuario is not None:
            return HttpResponse("exito",status=200)
        else:
            return HttpResponse("fallido",status=404)
       
class CrearPaciente(View):
    def post(self, request):
        datos  = json.loads(request.body)
        
        try:
            Paciente.objects.create(
                username = datos["nombres"],
                email = datos["email"],
                password = datos["contrasena"],
                ap_paterno = datos["apPaterno"],
                ap_materno = datos["apMaterno"],
                celular = datos["celular"]
            )
            return HttpResponse("creado con exito",status=200)
        except IntegrityError:
            return HttpResponse("error",status=400)
          
             
            
        
        
# class LoginView(View):
#     def post(self,request):
#         jd = json.loads(request.body)
#         email = jd['email']
#         password = jd['password']
#         # print(email,password)
#         user  = authenticate(username=email,password=password)
#         if user is not None:
#             user_data={
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#                 "avatar":user.avatar
#             }
#             return JsonResponse({"success":user_data}, status=200)
#         else:
#             return HttpResponse("login failed.", status=401)