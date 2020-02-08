from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('search/content/', views.ContentFetcher.as_view()),
    path('search/page/', views.ContentPageFetcher.as_view()),
    path('fetch/keyword/', views.KeywordAnalysis.as_view()),
    path('fetch/sentiment/', views.SentimentAnalysis.as_view()),
    path('fetch/tone/', views.ToneAnalysis.as_view()),
    path('fetch/visuals/', views.VisualAnalysis.as_view()),
    path('fetch/analysis/', views.WholeAnalysis.as_view())

]