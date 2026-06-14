from django.urls import path
from . import views

app_name = 'simple_blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.show, name='show'),
    path('article/create/', views.create, name='create'),
    path('article/<int:id>/update/', views.update, name='update'),
    path('article/<int:id>/delete/', views.delete, name='delete'),
    path('comments/<int:id>/update/', views.comment_update, name='comment_update'),
    path('author/<int:id>/', views.author, name='author'),
]
