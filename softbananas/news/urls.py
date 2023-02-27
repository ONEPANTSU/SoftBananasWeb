from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", views.news, name="news"),
    path("create", views.create_news, name="create_news"),
    path("<int:pk>", views.NewsDetailView.as_view(), name="news-detail"),
    path("<int:pk>/update", views.NewsUpdateView.as_view(), name="news-update"),
    path("<int:pk>/delete", views.NewsDeleteView.as_view(), name="news-delete"),
]
