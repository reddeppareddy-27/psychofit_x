from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render

def exercises_page(request):
    return render(request, 'exercises.html')

class MuscleGroupViewSet(viewsets.ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

class ExerciseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all().prefetch_related(
        'equipment_required',
        'animations',
        'variations'
    )
    serializer_class = ExerciseSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by muscle group
        muscle_group = self.request.query_params.get('muscle_group')
        if muscle_group:
            queryset = queryset.filter(
                models.Q(primary_muscle_group__name__icontains=muscle_group) |
                models.Q(secondary_muscle_group__name__icontains=muscle_group)
            )
            
        # Filter by category
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name__icontains=category)
            
        return queryset