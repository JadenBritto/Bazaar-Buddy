from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('regular', 'Regular User'),
        ('supplier', 'Supplier'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='regular')
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(('email address'), unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True )
    
    
    
    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

