from operator import index
from django.urls import path, include
from articles import views

urlpatterns = [
    
    path('', views.ArtcleList.as_view(), name="index"),
    path('<int:article_id>/', views.ArticletDetail.as_view(), name="article_view"),
]
