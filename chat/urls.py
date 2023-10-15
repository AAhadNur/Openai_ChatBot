from django.urls import path

from chat.views import chatbot, home

urlpatterns = [
    path('', home, name="home"),
    path('chat/', chatbot, name="chatbot"),
]
