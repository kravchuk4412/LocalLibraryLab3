from rest_framework import generics
#from rest_framework.permissions import 
from library.models import Book, BookInstance, Author
from .serializers import BookSerializer, BookInstanceSerializer, AuthorSerializer
from .permissions import IsStaff, IsStaffOrSafeMethod


class BookListView(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsStaffOrSafeMethod]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsStaff]


class BookInstanceListView(generics.ListCreateAPIView):
	queryset = BookInstance.objects.all()
	serializer_class = BookInstanceSerializer
	permission_classes = [IsStaff]


class BookInstanceDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = BookInstance.objects.all()
	serializer_class = BookInstanceSerializer
	permission_classes = [IsStaff]


class AuthorListView(generics.ListCreateAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
	permission_classes = [IsStaffOrSafeMethod]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
	permission_classes = [IsStaff]


class MyBooksListView(generics.ListAPIView):
	serializer_class = BookInstanceSerializer

	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user.id)


class BorrowedBooksListView(generics.ListAPIView):
	permission_classes = [IsStaff]
	serializer_class = BookInstanceSerializer

	def get_queryset(self):
		return BookInstance.objects.filter(status='o')