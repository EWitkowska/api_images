from django.db import models
from django.contrib.auth.models import User
from PIL import Image as img

# Create your models here.

def user_directory_path(instance, filename):

    return 'images/{0}'.format(filename)

class Profile(models.Model):

    OPTIONS = (
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ENTERPRISE', 'Enterprise')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=OPTIONS ,default='BASIC')

    def __str__(self):

        return f"{str(self.user)}"

class Image(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=user_directory_path, null=False, blank=False)
    thumbnail_200 = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    thumbnail_400 = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img_200 = img.open(self.image.path)
        img_400 = img.open(self.image.path)

        output_size_200 = (200, 200)
        output_size_400 = (400, 400)
        img_200.thumbnail(output_size_200)
        img_400.thumbnail(output_size_400)
        img_200.save(self.thumbnail_200.path)
        img_400.save(self.thumbnail_400.path)

    def __str__(self):

        return f"{self.name}"
    
# class Account(models.Model):

#     account_type = models.CharField(max_length=100, null=True, blank=True)
#     thumbnail_height = models.IntegerField()
#     thumbnail_width = models.IntegerField()
#     original_image = models.ImageField(upload_to='images/', null=True, blank=True)
#     # expiring_link = 

#     def __str__(self):

#         return f"{self.account_type}"