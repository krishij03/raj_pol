from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('detection.urls')),
    url(r'^api/', include(('alertupload_rest.urls', 'alertupload_rest'), namespace='api')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
