from django.urls import path

from user.views import loginPage, logoutPage, registerPage

urlpatterns = [
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('logout', logoutPage, name='logout'),
]
