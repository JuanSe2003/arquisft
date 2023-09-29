from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('citas/', views.variable_list, name='citaList'),
    path('citacreate/', csrf_exempt(views.variable_create), name='citaCreate'),
]