from django.shortcuts import render
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
