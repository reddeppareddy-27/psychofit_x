from django.db import models
from django.core.validators import RegexValidator


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensures state names are unique

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # States are ordered alphabetically
        verbose_name = "State"
        verbose_name_plural = "States"


class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="districts")  # Link to State

    def __str__(self):
        return f"{self.name}, {self.state.name}"  # Displays district with its state

    class Meta:
        ordering = ['name']  # Districts ordered alphabetically
        verbose_name = "District"
        verbose_name_plural = "Districts"
        unique_together = ('name', 'state')  # Prevent duplicate district names in the same state


class City(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="cities")  # Link to District

    def __str__(self):
        return f"{self.name}, {self.district.name}"  # Displays city with its district

    class Meta:
        ordering = ['name']  # Cities ordered alphabetically
        verbose_name = "City"
        verbose_name_plural = "Cities"
        unique_together = ('name', 'district')  # Prevent duplicate city names in the same district


class Gym(models.Model):
    image = models.ImageField(upload_to='gym_images/', null=True, blank=True, default=None)  # Optional gym image
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(regex=r'^\+?\d{9,15}$', message="Enter a valid phone number.")  # Phone validation
        ]
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="gyms")  # Link to City
    google_maps_link = models.URLField()  # Gym's location on Google Maps

    def __str__(self):
        return f"{self.name} in {self.city.name}"  # Displays gym name with its city

    class Meta:
        ordering = ['name']  # Gyms ordered alphabetically
        verbose_name = "Gym"
        verbose_name_plural = "Gyms"
