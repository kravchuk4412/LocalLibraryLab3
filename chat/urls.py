from django.urls import path

from . import views

urlpatterns = [
    path('', views.LibraryChatView.as_view(), name='library_chat'),
]