from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class profile(models.Model) :
    # One User Can Have Only One Profile and One Profile Can Have Only One User
    # Cascade means If We Delete User the Profile Will also be deleted
    user = models.OneToOneField(User,on_delete=models.CASCADE)  # Displaying User In Admin Panel With Image To Update
    image = models.ImageField(default='default.png',upload_to='LoginSYS/Images')

    def __str__(self) :
        return self.user.username

    # Resize the image 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        #To resize the profile image
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)