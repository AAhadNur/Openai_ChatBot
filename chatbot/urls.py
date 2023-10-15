
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # chat app
    path('', include('chat.urls')),

    # user app
    path('user/', include('user.urls')),
]
