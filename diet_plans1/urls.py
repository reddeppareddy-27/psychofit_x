from django.urls import path
from diet_plans.views import diet_plan_view

urlpatterns = [
    path('diet-plan1/', diet_plan_view, name='diet_plan1'),
]
