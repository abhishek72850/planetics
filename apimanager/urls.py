from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('fetch/post/', views.SocialFetcher.as_view()),
    path('fetch/keyword/', views.KeywordAnalysis.as_view()),
    path('fetch/sentiment/', views.SentimentAnalysis.as_view()),
    path('fetch/tone/', views.ToneAnalysis.as_view()),
    path('fetch/visuals/', views.VisualAnalysis.as_view())
]