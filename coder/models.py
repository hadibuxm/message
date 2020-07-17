from django.db import models
from django.urls import reverse # new

# Create your models here.
class Code(models.Model):
    roll_no=models.CharField(max_length=200)
    message=models.TextField()
    """
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )
    """
    def __str__(self):
        return self.roll_no
    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])