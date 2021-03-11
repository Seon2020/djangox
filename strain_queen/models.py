from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

strain_types = (
    ('Indica', 'INDICA'),
    ('Hybrid', 'HYBRID'),
    ('Sativa', 'SATIVA'),
)

class Strain(models.Model):
    name = models.CharField(max_length=64)
    strain_type = models.CharField(max_length=6, choices=strain_types)
    description = models.TextField(default='')
    smoker = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('strain_detail', args=[str(self.id)])