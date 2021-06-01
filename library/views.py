from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Book, BookInstance, Author
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_staff


class LibraryView(TemplateView):
	template_name = "library/library.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['books_count'] = Book.objects.all().count()
		context['authors_count'] = Author.objects.all().count()
		context['book_instances_count'] = BookInstance.objects.all().count()
		context['available_books_count'] = BookInstance.objects.filter(status__exact='a').count()
		return context


class BookListView(ListView):
	model = Book
	context_object_name = 'book_list'
	template_name = "library/books.html"
	

class AuthorListView(ListView):
	model = Author
	context_object_name = 'author_list'
	template_name = "library/authors.html"


class BorrowedBooksListView(StaffRequiredMixin, ListView):
	permission_required = 'library.can_mark_returned'
	model = BookInstance
	context_object_name = 'borrowedbook_list'
	template_name = "library/borrowed_books.html"

	def get_queryset(self):
		return BookInstance.objects.filter(status__exact='o').order_by('due_back')


class BookDetailView(DetailView):
	model = Book
	context_object_name = 'book'
	template_name = "library/book_detail.html"


class AuthorDetailView(DetailView):
	model = Author
	context_object_name = 'author'
	template_name = "library/author_detail.html"


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
	model = BookInstance
	context_object_name = 'mybook_list'
	template_name ='library/mybooks.html'

	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')