from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Movie, List
from django.contrib.auth.decorators import login_required


def movie_list(request):
    lists = List.objects.all()
    return render(request, 'movieapp/movie_list.html', {'lists': lists})
