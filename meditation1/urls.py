from django.urls import path
from meditation1.views import meditation_view

urlpatterns = [
    path('meditation/', meditation_view, name='meditation'),
]
