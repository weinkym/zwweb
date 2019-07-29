from django.urls import path

from . import views
from . import update

#wx
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:index>', views.test, name='test'),
    path('update/validity/', update.updateValidity, name='update.updateValidity'),
]