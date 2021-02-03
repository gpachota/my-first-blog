from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('lists/', views.list_of_lists, name='list_of_lists'),
    # path('lists/', views.movie_list, name='movie_list'),
]