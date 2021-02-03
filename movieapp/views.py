from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import List
from django.contrib.auth.decorators import login_required


@login_required()
def list_of_lists(request):
    lists = List.objects.filter(created_by=request.user)
    return render(request, 'movieapp/list_of_lists.html', {'lists': lists})


@login_required()
def movie_list(request):
    pass


def main_page(request):
    return render(request, 'movieapp/main_page.html')
