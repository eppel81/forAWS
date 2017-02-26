from django.views.generic import TemplateView, FormView, ListView

from .forms import UploadPhotoForm
from .models import Photo


class IndexView(TemplateView):
    template_name = 'photos/index.html'


class PhotoListView(ListView):
    queryset = Photo.objects.all()
    template_name = 'photos/all-photos.html'


class UploadPhotoView(FormView):
    form_class = UploadPhotoForm
    template_name = 'photos/upload-photo.html'
    success_url = '/'

    def form_valid(self, form):
        photo = form.save()
        return super(UploadPhotoView, self).form_valid(form)

