from operator import index
from django.urls import path, include
from articles import views

urlpatterns = [
    
    path('', views.articleAPI, name="index"),
    path('<int:article_id>/', views.articledetailAPI, name="article_view"),
]
