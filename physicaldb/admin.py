from django.contrib import admin
from django import forms
from .models import *

@admin.register(MuscleGroup)
class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')

@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'home_alternative')

@admin.register(ViewAngle)
class ViewAngleAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_editable = ('code',)

class ExerciseEquipmentInline(admin.TabularInline):
    model = ExerciseEquipment
    extra = 1

class ExerciseAnimationForm(forms.ModelForm):
    class Meta:
        model = ExerciseAnimation
        fields = '__all__'
    
    view_angles = forms.ModelMultipleChoiceField(
        queryset=ViewAngle.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    variations = forms.ModelMultipleChoiceField(
        queryset=ExerciseVariation.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class ExerciseAnimationInline(admin.TabularInline):
    model = ExerciseAnimation
    form = ExerciseAnimationForm
    extra = 1
    filter_horizontal = ('view_angles', 'variations')

@admin.register(ExerciseAnimation)
class ExerciseAnimationAdmin(admin.ModelAdmin):
    form = ExerciseAnimationForm
    list_display = ('exercise', 'get_animation_type_display', 'get_view_angles', 'get_variations')
    list_filter = ('animation_type', 'exercise__category')
    filter_horizontal = ('view_angles', 'variations')
    
    def get_view_angles(self, obj):
        return ", ".join([angle.name for angle in obj.view_angles.all()])
    get_view_angles.short_description = 'View Angles'
    
    def get_variations(self, obj):
        return ", ".join([variation.name for variation in obj.variations.all()])
    get_variations.short_description = 'Variations'

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'primary_muscle_group')
    list_filter = ('category', 'difficulty', 'primary_muscle_group')
    search_fields = ('name', 'description')
    inlines = [ExerciseEquipmentInline, ExerciseAnimationInline]

@admin.register(ExerciseVariation)
class ExerciseVariationAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_exercise', 'difficulty_adjustment')
    list_filter = ('base_exercise', 'difficulty_adjustment')
    search_fields = ('name', 'description')