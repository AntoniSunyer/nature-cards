from django.db import models
from django.conf import settings
import uuid
from PIL import Image
import os

# Create your models here.

# Genera un nom aleatori pel nom del fitxer de la imatge
def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

# creates a thumbnail of an existing image
def create_thumbnail(input_image, thumbnail_size=(256, 256)):
    # make sure an image has been set
    if not input_image or input_image == "":
        return

    # open image
    image = Image.open(input_image)

    # use PILs thumbnail method; use anti aliasing to make the scaled picture look good
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)

    # parse the filename and scramble it
    filename = scramble_uploaded_filename(None, os.path.basename(input_image.name))
    arrdata = filename.split(".")
    # extension is in the last element, pop it
    extension = arrdata.pop()
    basename = "".join(arrdata)
    # add _thumb to the filename
    new_filename = basename + "_thumb." + extension

    # save the image in MEDIA_ROOT and return the filename
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename


class NatureCard(models.Model):
    name = models.CharField(max_length=255, blank=True, default='No name')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='cards', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class NatureImage(models.Model):
    image = models.ImageField("Nature image", upload_to=scramble_uploaded_filename)
    thumbnail = models.ImageField("Thumbnail of nature image", blank=True)
    title = models.CharField(max_length=255, blank=True, default='No title')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey(NatureCard, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # generate and set thumbnail or none
        self.thumbnail = create_thumbnail(self.image)
        super(NatureImage, self).save()

    def __str__(self):
        return self.title



