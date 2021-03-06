from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    
    def __str__(self):
        return str(self.user)
