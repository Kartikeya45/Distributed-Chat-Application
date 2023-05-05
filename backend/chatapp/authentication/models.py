from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length = 100)
    receiver = models.CharField(max_length = 100)
    key = models.CharField(max_length=20)
    body = models.CharField(max_length = 1000)
    timestep = models.DateTimeField(auto_now_add=True, blank=True)
    group = models.BooleanField()

    # def __str__(self):
    #     return f"{sender} -> {"


class UserDetails(models.Model):
    name = models.CharField(max_length=100, default="default_name")
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    #chats = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)
