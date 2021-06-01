from django.shortcuts import render
from .tasks import mailing_task, stat_task
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_staff


class TasksTableView(StaffRequiredMixin, TemplateView):
	template_name = 'tasks/tasks_table.html'


class StatTaskView(StaffRequiredMixin, TemplateView):
	def get(self, request, *args, **kwargs):
		stat_task.delay()
		return render(request, 'tasks/stat.html', {
			'response': 'Your task for site statistic was started.'
		})


class MailingTaskView(StaffRequiredMixin, TemplateView):
	def get(self, request, *args, **kwargs):
		mailing_task.delay("Hello", "Hello, how are you?", 1)
		return render(request, 'tasks/mailing.html', {
			'response': 'Your task for group mailing was started.'
		})
