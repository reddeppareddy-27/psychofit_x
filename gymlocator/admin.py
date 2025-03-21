from django.contrib import admin
from .models import State, District, City, Gym

# Register your models here
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Columns displayed in the admin list
    search_fields = ('name',)      # Enable searching by name
    ordering = ('name',)           # Sort states alphabetically

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state')  # Display associated state
    search_fields = ('name',)
    list_filter = ('state',)               # Add a filter for states

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'district')  # Display associated district
    search_fields = ('name',)
    list_filter = ('district',)               # Add a filter for districts

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'phone_number')  # Display key gym info
    search_fields = ('name', 'phone_number')               # Enable searching
    list_filter = ('city',)                                # Filter by city
