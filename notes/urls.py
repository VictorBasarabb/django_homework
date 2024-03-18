from django.urls import path

from notes.views import homepage


urlpatterns = [
    path('', homepage, name='homepage'),
]