from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/search/', views.search, name="search"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)