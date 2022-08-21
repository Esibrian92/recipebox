from django.shortcuts import render

from recipeboxapp.models import Recipe
from recipeboxapp.models import Author
# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    return render(request, "homepage.html", {'recipes': recipes})
    # author = Author.get(id=Author)


def recipe_details(request, recipe_id: int):
    current_recipe = Recipe.objects.filter(id=recipe_id)
    return render(request, "recipe_details.html", {'recipe': current_recipe})


def author_details(request, author_id: int):
    current_author = Author.objects.get(id=author_id)
    return render(request, "author_details.html", {'author': current_author})
