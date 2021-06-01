from django.db import models
from django.urls import reverse
from datetime import date
from user_accs.models import CustomUser


class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('author_detail', args=[str(self.id)])

	def __str__(self):
		return '{0}, {1}'.format(self.last_name, self.first_name)


class Book(models.Model):
	GENRE = (
		('fantasy', 'Fantasy'),
		('sci-fi', 'Science Fiction'),
		('adventure', 'Adventure'),
		('hi-fi', 'Historical fiction'),
		('romance', 'Romance'),
		('thriller', 'Thriller'),
	)
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000)
	genre = models.CharField(max_length=40,
							 choices=GENRE,
	)

	class Meta:
		ordering = ['title', 'author']

	def get_absolute_url(self):
		return reverse('book_detail', args=[str(self.id)])

	def __str__(self):
		return self.title


class BookInstance(models.Model):
	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)
	book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
	due_back = models.DateField(null=True, blank=True)
	borrower = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

	def is_overdue(self):
		return self.due_back and date.today() > self.due_back

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='d')

	class Meta:
		ordering = ['due_back']
		permissions = (("can_mark_returned", "Set book as returned"),)

	def __str__(self):
		return '{0} ({1})'.format(self.id, self.book.title)
