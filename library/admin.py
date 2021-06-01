from django.contrib import admin
from .models import Author, Book, BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	model = Book
	list_display = ('title', 'author', 'genre')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	model = Author
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	model = BookInstance
	list_display = ('book', 'status', 'borrower', 'due_back',)