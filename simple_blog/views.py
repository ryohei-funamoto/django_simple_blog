from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-created_at')

    context = {
        'articles': articles,
    }

    return render(
        request,
        'simple_blog/index.html',
        context=context,
    )

def show(request, id):
    article = get_object_or_404(Article, pk=id)

    context = {
        'article': article,
    }

    return render(
        request,
        'simple_blog/detail.html',
        context=context,
    )
