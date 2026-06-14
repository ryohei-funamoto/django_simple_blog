from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

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
    comments = Comment.objects.filter(article__id=article.id).order_by('-created_at')
    form = CommentForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.article = article
                comment.save()

                return redirect('simple_blog:show', id=article.id)

    context = {
        'article': article,
        'comments': comments,
        'form': form,
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

@login_required
def update(request, id):
    article = get_object_or_404(Article, pk=id)
    form = ArticleForm(request.POST or None, instance=article)

    if request.user == article.user:
        if request.method == 'POST':
            if form.is_valid():
                form.save()

                return redirect('simple_blog:show', id=article.id)

        context = {
            'article': article,
            'form': form,
        }

        return render(
            request,
            'simple_blog/update.html',
            context=context,
        )
    else:
        raise PermissionDenied

@login_required
def delete(request, id):
    article = get_object_or_404(Article, pk=id)

    if request.user == article.user:
        if request.method == 'POST':
            article.delete()

            return redirect('simple_blog:index')

        context = {
            'article': article,
        }

        return render(
            request,
            'simple_blog/detail.html',
            context=context,
        )
    else:
        raise PermissionDenied

def author(request, id):
    User = get_user_model()
    author = get_object_or_404(User, pk=id)

    articles = Article.objects.filter(user_id=author.id).order_by('-created_at')

    context = {
        'author': author,
        'articles': articles,
    }

    return render(
        request,
        'simple_blog/author.html',
        context=context,
    )
