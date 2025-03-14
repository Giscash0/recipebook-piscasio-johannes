from django.urls import path
from .views import recipe_list, recipe

urlpatterns = [
    path('recipes/list', recipe_list.as_view(), name='recipe_list'),
    path('recipe/<int:num>', recipe.as_view(), name='recipe'),
]