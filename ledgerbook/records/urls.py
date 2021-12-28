from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecordList, name='recordList'),
]