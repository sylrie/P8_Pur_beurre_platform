""" urls for product app"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.Product().results, name='products'),
    path('substitutes/', views.Product().substitutes, name='substitutes'),
    path('food/', views.Product().food, name='food'),
    path('favorites/', views.Product().change_favorite, name='change_favorite'),
    path('favorites/', views.Product().favorites, name='favorites'),
    path('legals/', views.legals, name='legals'),
]
