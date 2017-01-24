from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from photo import views

urlpatterns = [
    url(r'^photos/$', views.photos),
    url(r'^photo/(?P<photo_id>\d+)/$', views.photo),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)