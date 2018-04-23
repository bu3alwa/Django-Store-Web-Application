from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = list(Article.objects.all())
    return render(request, 'articles/index.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.filter(slug=slug).first()
    return render(request, 'articles/article.html', {'article': article})
    

