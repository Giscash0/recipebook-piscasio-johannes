from django.urls import path
from .views import RecipeList, RecipeDetail

urlpatterns = [
    path('recipes/list', RecipeList.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetail.as_view(), name='recipe'),
]