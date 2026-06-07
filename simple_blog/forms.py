from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        labels = {
            'title': 'タイトル',
            'content': '本文',
        }
