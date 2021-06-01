from django.urls import path
from .views import (LibraryView, BookListView, AuthorListView, BorrowedBooksListView,
 				    BookDetailView, AuthorDetailView, LoanedBooksByUserListView,)


urlpatterns = [
	path('', LibraryView.as_view(), name='library'),
	path('books/', BookListView.as_view(), name='books'),
	path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
	path('authors/', AuthorListView.as_view(), name='authors'),
	path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
	path('mybooks/', LoanedBooksByUserListView.as_view(), name='mybooks'),
	path('borrowedbooks/', BorrowedBooksListView.as_view(), name='borrowedbooks'),
]
