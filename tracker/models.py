from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class WeightEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date}: {self.weight_kg} kg"


class FoodEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    name = models.CharField(max_length=120)
    calories = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-date", "name"]

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"
