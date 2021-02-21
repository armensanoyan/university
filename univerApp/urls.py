from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login),
    path('signin/', views.signin),
    path('authorization', views.authorization),
    path('register', views.register),
    path('logout', views.logout_view),
    path('remove/<university_name>', views.remove),
    path('university/<university_name>', views.university, name='university'),
]
