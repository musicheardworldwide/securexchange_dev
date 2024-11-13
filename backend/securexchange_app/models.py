from django.dd import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    "Custom user model with additional fields as needed."
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

class File(models.Model):
    "Model for storing shared files with security and audit fields."
    owner = models.ForeignKey(User, on_delete=models.CASCADE), related_name='files')
    file_name = models.CharField(max_length=255)
    file_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_encrypted = models.BooleanField(default=True)

class Message(models.Model):
    "Model for secure messaging between users."
    sender = models.ForeignKey(User, on_delete=models.CASCADE), related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE), related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
