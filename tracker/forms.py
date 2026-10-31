from django import forms
from .models import FoodEntry, WeightEntry


class WeightEntryForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ["date", "weight_kg", "note"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}


class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ["date", "name", "calories"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}
