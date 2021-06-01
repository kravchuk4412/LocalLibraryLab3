from django.db import models

class ConnectedUsers(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length = 70)
    username = models.CharField(max_length = 70)
    connected = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s %s aka %s#%s" % (self.first_name, self.last_name, self.username, self.id)