import datetime
import json
from django.utils import timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from library.models import Author, Book
from django.shortcuts import get_object_or_404
from chat.models import ConnectedUsers


class LibraryChatView(LoginRequiredMixin, TemplateView):
	template_name = 'chat/library_chat.html'
	login_url = 'login'

	def get_context_data(self):
		context = super().get_context_data()
		context['room_name'] = 'library_chat'
		context['connected_users'] = ConnectedUsers.objects.all()
		context['authors'] = Author.objects.all()
		context['books'] = Book.objects.all()
		return context