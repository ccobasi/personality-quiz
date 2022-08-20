from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import personality


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personality/', include(personality.urls, namespace="personality"))
]

# urlpatterns+= static(settings.STATIC_URL, document_root=settings.)
