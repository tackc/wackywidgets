from django.db import models
from django.urls import reverse

# Create your models here.

class Widget(models.Model):
    description = models.CharField(max_length=75)
    quantity = models.IntegerField(max_length=3)

# description - a CharField with a max_length of your choosing
# quantity - an IntegerField

    def __str__(self):
        return self.description

    # def get_absolute_url(self):
    #     return reverse('tools_detail', kwargs={'description_id': self.id})