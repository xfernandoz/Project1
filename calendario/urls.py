from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('/<int:year>/<str:month>/', views.calendario, name='calendario'),
    path('/agregar_evento/', views.agregar_evento, name='agregar-evento'),
]