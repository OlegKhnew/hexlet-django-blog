from django.shortcuts import render
from django.http import HttpResponse


ARTICLES = [{'title':'Article 1 - title', 'content': 'Article 1 content'},
            {'title':'Article 2 - title', 'content': 'Article 2 content'}]

#def index(request):
#    return HttpResponse('article')

def index(request):
    return render(request, 'indexarticles.html', context={'articles':ARTICLES})

# Create your views here.
