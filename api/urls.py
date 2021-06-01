from django.urls import path
from .views import (BookDetailView, BookListView, AuthorDetailView, 
					AuthorListView, MyBooksListView, BorrowedBooksListView,
					BookInstanceListView, BookInstanceDetailView,)

urlpatterns = [
	path('books/<int:pk>/', BookDetailView.as_view()),
	path('books/', BookListView.as_view()),
	path('authors/<int:pk>/', AuthorDetailView.as_view()),
	path('authors/', AuthorListView.as_view()),
	path('copies/<int:pk>/', BookInstanceDetailView.as_view()),
	path('copies/', BookInstanceListView.as_view()),
	path('books/mybooks/', MyBooksListView.as_view()),
	path('books/borrowedbooks/', BorrowedBooksListView.as_view()),
]
