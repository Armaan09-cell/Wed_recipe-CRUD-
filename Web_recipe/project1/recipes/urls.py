from django.contrib import admin
from django.urls import path
from recipes.views import *

urlpatterns = [
    path('recipe/', recipe, name='recipe'),
    path('delete-recipe/<id>/', delete_recipe, name="delete_recipe"),
    path('update-recipe/<id>/', update_recipe, name="update_recipe"),
]
