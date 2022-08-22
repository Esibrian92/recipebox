"""recipeboxsettings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipeboxapp import views
import recipeboxapp
from recipeboxapp.views import index
from recipeboxapp.views import recipe_details
from recipeboxapp.views import author_details
# from recipeboxapp.views import recipes

urlpatterns = [
    path("", views.index,),
    path("recipe_details/<int:recipe_id>/", views.recipe_details),
    path("author_details/<int:author_id>/", views.author_details),
    # path("recipes/<int:author_id>/", views.recipes),
    path('admin/', admin.site.urls),
]
