from django.urls import path
from . import views

app_name = 'main_feed'
urlpatterns = [
    path('', views.MainFeedView.as_view(), name='index'),
]
