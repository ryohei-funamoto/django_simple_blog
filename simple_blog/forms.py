from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        labels = {
            'title': 'タイトル',
            'content': '本文',
        }
        error_messages = {
            'title': {
                'required': 'タイトルを入力してください',
            },
            'content': {
                'required': '本文を入力してください',
            },
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'コメント',
        }
        error_messages = {
            'content': {
                'required': 'コメントを入力してください',
            },
        }
