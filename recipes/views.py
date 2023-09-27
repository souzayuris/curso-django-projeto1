from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.pagination import make_pagination_range
from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    # recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')

    recipes = get_list_or_404(Recipe.objects.filter(is_published=True).order_by('-id'))

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        current_page
    )

    return render(request, 'recipes/pages/home.html', context={
        'recipes' : page_obj,
        'pagination_range': pagination_range
    })

def category(request, category_id):
    # recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')

    # if not recipes:
    #     raise Http404('Not found ')

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category_id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes' : recipes,
        'title': f'{recipes[0].category.name} - Category | ',
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q')

    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        # where title like search_term
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
    

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes':recipes,
    })