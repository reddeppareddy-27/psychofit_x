from django.db import models

class MuscleGroup(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ExerciseCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    home_alternative = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    DIFFICULTY_LEVELS = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
        ('P', 'Professional'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ExerciseCategory, on_delete=models.SET_NULL, null=True)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_LEVELS, default='B')
    primary_muscle_group = models.ForeignKey(
        MuscleGroup, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='primary_exercises'
    )
    secondary_muscle_group = models.ForeignKey(
        MuscleGroup, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='secondary_exercises'
    )
    calories_burned_per_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    equipment_required = models.ManyToManyField(Equipment, through='ExerciseEquipment')
    
    def __str__(self):
        return self.name

class ExerciseEquipment(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    required = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('exercise', 'equipment')
    
    def __str__(self):
        return f"{self.exercise.name} - {self.equipment.name}"

class ViewAngle(models.Model):
    """Model to store available view angles for animations"""
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.name

class ExerciseAnimation(models.Model):
    ANIMATION_TYPES = [
        ('3D', '3D Animation'),
        ('2D', '2D Animation'),
        ('VID', 'Video'),
    ]
    
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='animations')
    animation_file = models.FileField(upload_to='exercise_animations/%Y/%m/%d/')
    animation_type = models.CharField(max_length=3, choices=ANIMATION_TYPES)
    view_angles = models.ManyToManyField(ViewAngle)
    variations = models.ManyToManyField('ExerciseVariation', blank=True)
    duration_seconds = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.exercise.name} - {self.get_animation_type_display()}"

class ExerciseVariation(models.Model):
    base_exercise = models.ForeignKey(
        Exercise, 
        on_delete=models.CASCADE,
        related_name='variations'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty_adjustment = models.IntegerField(
        help_text="-1 for easier, 0 for same, +1 for harder",
        default=0
    )
    
    def __str__(self):
        return f"{self.base_exercise.name} - {self.name}"