from django.urls import path

from . import views
#wx
urlpatterns = [
    path('', views.index, name='index'),
]