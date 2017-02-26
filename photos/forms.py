from django.forms import ModelForm

from .models import Photo


class UploadPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', ]
