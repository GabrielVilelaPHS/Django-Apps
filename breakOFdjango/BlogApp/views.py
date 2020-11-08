from django.shortcuts import render

from .models import Post

# Create your views here.

def home(request):

    return render(request, 'pages/home.html')

def page(request):
    '''
    pega todos os objetos que vãoe estar no models.py,
    ou seja, pega todos os posts criados no banco de dados
    '''
    posts = Post.objects.all().order_by('created_at') 

    return render(request, 'pages/index.html', {'posts':posts}) #o terceiro argumento cria um dicionario aqui