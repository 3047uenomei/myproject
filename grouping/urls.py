from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_views, name='group_view'),
]