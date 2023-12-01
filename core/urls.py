from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from store.admin import store_site

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('admin/', include('custom_admin.urls')),
    
    path('', include('store.urls', namespace='store')),
    path('basket/',include('basket.urls',namespace='basket')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
