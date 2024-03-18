from django.urls import path

from notes.views import note


urlpatterns = [
    path('', note, name='note'),
]