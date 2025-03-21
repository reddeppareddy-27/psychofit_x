from django.urls import path
from privacy.views import *

urlpatterns=[
    path('privacy-policy/',privacy,name="privacy"),
]