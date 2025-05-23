from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeCreate, RecipeImageCreate

urlpatterns = [
    path('recipes/list', RecipeList.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetail.as_view(), name='recipe'),
    path('recipe/add', RecipeCreate.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image', RecipeImageCreate.as_view(), name='recipe_add_image'),
]