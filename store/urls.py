from django.conf.urls import url
from django.conf.urls.static import static
from musique import settings

from . import views

app_name="store"
urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)