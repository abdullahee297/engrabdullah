<<<<<<< HEAD
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
=======
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
>>>>>>> bcabad9afcce1d08ec24b6a85be487c198b25228
    created_at = models.DateTimeField(auto_now_add=True)