from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from io import BytesIO
from django.core.files.base import ContentFile

class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User, # settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = models.ImageField(default='default.jpg', upload_to='pics')

    MAX_IMAGE_SIZE = 300

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'

    def save(self, *args, **kwargs):
        # bw_image = Image.open(self.image).convert('L')
        #
        # new_image_io = BytesIO()
        # bw_image.save(new_image_io, format='png')
        #
        # self.image.save(name='image.jpg',
        #                 content=ContentFile(new_image_io.getvalue()),
        #                 save=False
        #                 )
        #
        # super().save(*args, **kwargs)

# class UserProfile2(User):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,
#                                 on_delete=models.CASCADE,
#                                 related_name="profile2", parent_link=True)
#     image = models.ImageField(default='default.jpg', upload_to='pics')
#
#     MAX_IMAGE_SIZE = 300
#
#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name} Profile'
#
#     def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > self.MAX_IMAGE_SIZE or img.width > self.MAX_IMAGE_SIZE:
            output_size = (self.MAX_IMAGE_SIZE, self.MAX_IMAGE_SIZE)
            img.thumbnail(output_size)
            img.save(self.image.path)
