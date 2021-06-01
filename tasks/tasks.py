from django.core.mail import send_mass_mail
from asgiref.sync import async_to_sync
from celery import shared_task, Task
from user_accs.models import CustomUser
from channels.layers import get_channel_layer
from django.utils import timezone, dateformat
import time


class BaseTask(Task):
	task_name = "task_name"
	def on_success(self, retval, task_id, args, kwargs):
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
					"tasks", {
						"name" : self.task_name,
						"type" : "task",
						"task_id" : task_id,
						"args" : str(args),
						"result" : "Success!",
						"time" : "%s" % (dateformat.format(timezone.localtime(timezone.now()), "Y-m-d H:i:s")),
		})
		return super().on_success(retval, task_id, args, kwargs)

	def on_failure(self, exc, task_id, args, kwargs, einfo):
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
					"task", {
						"name" : self.task_name,
						"type" : "task",
						"task_id" : task_id,
						"args" : str(args),
						"result" : "Failure!",
						"time" : "%s" % (dateformat.format(timezone.localtime(timezone.now()), "Y-m-d H:i:s")),
		})
		return super().on_failure(exc, task_id, args, kwargs, einfo)


class StatTask(BaseTask):
	task_name = "stat_task"


class MailingTask(BaseTask):
	task_name = "mailing_task"


@shared_task(base=MailingTask)
def mailing_task(subject, message, group_id):
	mails = []
	receivers = CustomUser.objects.filter(group=group_id)
	
	for receiver in receivers:
		mails.append((subject, message, 'kravchuk@gmail.com', [receiver.email]))

	#send_mass_mail(mails)
	time.sleep(5)


@shared_task(base=BaseTask)
def stat_task():
	
	# Gathering statistic about library 

	time.sleep(5)
