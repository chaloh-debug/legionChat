from django.urls import path

from .views import friends, profile, requests


urlpatterns = [
    path("friends/", friends.as_view(), name="friends"),
    path("friends/profile", profile, name="profile"),
    path("friends/requests/", requests, name="requests"),    
]
