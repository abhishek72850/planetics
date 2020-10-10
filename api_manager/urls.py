from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('account/login', views.AccountLogin.as_view()),
    path('account/register', views.AccountRegister.as_view()),
    path('account/details', views.AccountDetails.as_view()),
    path('account/plan', views.AccountAssignOrUpdatePlan.as_view()),
    # path('account/subscribe', views.AccountSubscribeTopic.as_view()),
    path('account/change_password', views.AccountChangePassword.as_view()),
    path('account/forgot_password', views.GeneratePasswordResetLink.as_view()),
    path('account/reset_password', views.ResetPassword.as_view()),
    path('account/confirm_email', views.ConfirmEmail.as_view()),
    # path('account/unsubscribe', views.UnSubscribe.as_view()),
    # path('account/confirm_subscription', views.ConfirmSubscription.as_view()),
    # path('analysis/summary/', views.SummaryAnalysis.as_view()),
    path('search/content/', views.ContentFetcher.as_view()),
    path('search/page/', views.ContentPageFetcher.as_view()),
    path('fetch/keyword/', views.KeywordAnalysis.as_view()),
    path('fetch/sentiment/', views.SentimentAnalysis.as_view()),
    path('fetch/tone/', views.ToneAnalysis.as_view()),
    path('fetch/visuals/', views.VisualAnalysis.as_view()),
    path('fetch/analysis/', views.WholeAnalysis.as_view()),
    path('fetch/summary/', views.SummaryAnalysis.as_view())
]
