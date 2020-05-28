from django import forms
from django.db import models
from django.db.models.fields.files import ImageField


class Image(models.Model):
    upload_time = models.DateTimeField()
    image = ImageField(upload_to="uploads")


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("image",)
