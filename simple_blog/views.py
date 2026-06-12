from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

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

@login_required
def create(request):
    form = ArticleForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            return redirect('simple_blog:show', id=article.id)

    context = {
        'form': form,
    }

    return render(
        request,
        'simple_blog/create.html',
        context=context,
    )
