from django.urls import path
# Create your models here.
from .views import Login,CrearPaciente
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login',csrf_exempt(Login.as_view()), name="login"),
    path('signup',csrf_exempt(CrearPaciente.as_view()), name="crear"),
]