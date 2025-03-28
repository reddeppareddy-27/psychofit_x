from django.urls import path
from yoga1.views import yoga_plan_view

urlpatterns = [
    path('yoga/', yoga_plan_view, name='yoga'),
]