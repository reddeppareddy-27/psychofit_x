from rest_framework import serializers
from .models import *

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = '__all__'

class ExerciseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCategory
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class ExerciseAnimationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseAnimation
        fields = '__all__'

class ExerciseVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseVariation
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    category = ExerciseCategorySerializer()
    primary_muscle_group = MuscleGroupSerializer()
    secondary_muscle_group = MuscleGroupSerializer()
    equipment = EquipmentSerializer(many=True, read_only=True, source='equipment_required')
    animations = ExerciseAnimationSerializer(many=True, read_only=True)
    variations = ExerciseVariationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Exercise
        fields = '__all__'