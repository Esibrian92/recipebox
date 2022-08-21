from django.shortcuts import render

from recipeboxapp.models import Recipe
from recipeboxapp.models import Author
# Create your views here.


def index(request):
    recipe = Recipe.objects.all()
    return render(request, "homepage.html", {"recipe": recipe})
    # author = Author.get(id=Author)


def recipe_details(request, recipe_id: int):
    recipes = Recipe.objects.filter(id=recipe_id)
    return render(request, "recipe_details.html", {recipes: "recipes"})


def author_detail(request, author_id: int):
    current_author = Author.objects.get(id=author_id)
    return render(request, "author_details.html", {current_author: "current_user"})
