from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goGetTheGood/', views.goGetTheGood, name= 'go_get'),
    path('happyhappy/',views.happyhappyjoyjoy, name= 'happy_happy'),
]