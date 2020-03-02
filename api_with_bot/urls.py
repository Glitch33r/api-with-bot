from django.contrib import admin
from django.urls import path, include
from automate.views import automate_api
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sn/user/', include('user.urls')),
    path('api/sn/post/', include('post.urls')),
    path('auto-bot/', automate_api)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
