from django.shortcuts import render

def index(request):
    data = {
        'title': 'Home page',
    }
    return render(request, 'main/index.html', data)