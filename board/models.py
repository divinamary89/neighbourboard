from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('events', 'Events'),
    ('lostfound', 'Lost & Found'),
    ('notices', 'Notices'),
    ('recommendations', 'Recommendations'),
]

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title