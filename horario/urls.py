from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('horarios/', views.variable_list, name='horarioList'),
    path('horariocreate/', csrf_exempt(views.variable_create), name='horarioCreate'),
]