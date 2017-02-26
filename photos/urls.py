from django.conf.urls import url

from .views import IndexView, UploadPhotoView, PhotoListView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^all-photos/$', PhotoListView.as_view(), name='all-photos'),
    url(r'^upload-photo/$', UploadPhotoView.as_view(), name='upload-photo'),
]