from django.urls import path

from .views import request_info_view

urlpatterns = [
    path('request-info/', request_info_view, name='request_info'),
]
