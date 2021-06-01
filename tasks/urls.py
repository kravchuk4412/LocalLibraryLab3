from django.urls import path

from .views import TasksTableView, StatTaskView, MailingTaskView

urlpatterns = [
	path('tasks_table/', TasksTableView.as_view(), name='tasks_table'),
	path('stat_task/', StatTaskView.as_view(), name='stat_task'),
    path('mailing_task/', MailingTaskView.as_view(), name='mailing_task'),
]