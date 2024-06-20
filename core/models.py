from django.db import models
from django.contrib.auth.models import User

class YouTubeChannel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=100)

class Video(models.Model):
    channel = models.ForeignKey(YouTubeChannel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='videos/')
    approved = models.BooleanField(default=False)
    uploaded_to_youtube = models.BooleanField(default=False)

class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    channels = models.ManyToManyField(YouTubeChannel)

class Approval(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    date_approved = models.DateTimeField(null=True, blank=True)
