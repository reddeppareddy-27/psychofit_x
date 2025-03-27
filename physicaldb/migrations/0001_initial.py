# Generated by Django 5.1.7 on 2025-03-27 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('home_alternative', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ViewAngle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('difficulty', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('P', 'Professional')], default='B', max_length=1)),
                ('calories_burned_per_min', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='physicaldb.exercisecategory')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required', models.BooleanField(default=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physicaldb.equipment')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physicaldb.exercise')),
            ],
            options={
                'unique_together': {('exercise', 'equipment')},
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='equipment_required',
            field=models.ManyToManyField(through='physicaldb.ExerciseEquipment', to='physicaldb.equipment'),
        ),
        migrations.CreateModel(
            name='ExerciseVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('difficulty_adjustment', models.IntegerField(default=0, help_text='-1 for easier, 0 for same, +1 for harder')),
                ('base_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='physicaldb.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='primary_muscle_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_exercises', to='physicaldb.musclegroup'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='secondary_muscle_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondary_exercises', to='physicaldb.musclegroup'),
        ),
        migrations.CreateModel(
            name='ExerciseAnimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animation_file', models.FileField(upload_to='exercise_animations/%Y/%m/%d/')),
                ('animation_type', models.CharField(choices=[('3D', '3D Animation'), ('2D', '2D Animation'), ('VID', 'Video')], max_length=3)),
                ('duration_seconds', models.PositiveIntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animations', to='physicaldb.exercise')),
                ('variations', models.ManyToManyField(blank=True, to='physicaldb.exercisevariation')),
                ('view_angles', models.ManyToManyField(to='physicaldb.viewangle')),
            ],
        ),
    ]
