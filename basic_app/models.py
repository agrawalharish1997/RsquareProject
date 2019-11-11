from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user              =models.OneToOneField(User, on_delete=models.CASCADE,)
    #additional
    portfolio_site    =models.URLField(blank=True)
    profile_pic       =models.ImageField(upload_to='profile_pics',blank=True)
    aadhar_pic        =models.ImageField(upload_to='aadhar_pics',blank=True)
    drivinglicense_pic=models.ImageField(upload_to='license_pics',blank=True)

    def __str__(self):
        return self.user.username
