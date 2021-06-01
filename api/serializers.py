from rest_framework import serializers
from library.models import Book, BookInstance, Author 


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'title', 'summary', 'author', 'genre')


class BookInstanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookInstance
		fields = ('id', 'book', 'borrower', 'due_back', 'status')


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death')
