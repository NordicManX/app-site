from django.urls import path

from appsite.blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]
