from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

# Create your views here.



def index(request):

    
    context = {
        'title': 'Roga&Kopyta - Главная',
        'content': 'зоомагазин - Roga&Kopyta',
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Roga&Kopyta - O нас',
        'content': 'О нас',
        'text_on_page': 'Лучший магазин товаров для животных и их хозяев'
    }
    return render(request, 'main/about.html', context)


