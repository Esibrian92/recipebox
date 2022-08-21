from django.shortcuts import render

from recipeboxapp.models import Recipe
from recipeboxapp.models import Author
# Create your views here.


def index(request):
    recipe = Recipe.objects.all()
    return render(request, "homepage.html", {"recipe": recipe})
    # author = Author.get(id=Author)
