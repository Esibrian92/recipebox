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
    recipes = Recipe.objects.filter(author=current_author)
    return render(request, "author_details.html", {'author': current_author, 'recipes': recipes})


# def recipes(request, author_id: int):
#     this_author = Author.objects.get(id=author_id)
#     recipes = Recipe.objects.filter(author=this_author)
#     return render(request, "recipes.html", {'this_author': this_author}, {'recipes': recipes})
