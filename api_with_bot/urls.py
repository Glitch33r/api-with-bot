from django.contrib import admin
from django.urls import path, include
# from automate.views import automate_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sn/user/', include('user.urls')),
    path('api/sn/post/', include('post.urls')),
    # path('auto-bot/<str:type>', automate_api)
]
