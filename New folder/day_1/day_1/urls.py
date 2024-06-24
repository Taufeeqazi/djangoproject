
from django.contrib import admin
from django.urls import path
from day_1app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.Homepage),
    path('signup.html',v.SignupPage),
    path('login.html',v.loginPage)
]
