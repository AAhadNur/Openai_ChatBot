from django.urls import path

from chat.views import chatbot, loginPage, logoutPage, registerPage

urlpatterns = [
    path('', chatbot, name="chatbot"),

    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('logout', logoutPage, name='logout'),
]
