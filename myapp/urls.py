from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Home),
    path('login',views.loginpage),
    path('dashboard',views.dashboard),
    path('logout',views.logout1,name="logout")
]