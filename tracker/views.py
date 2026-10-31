from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import FoodEntryForm, WeightEntryForm
from .models import FoodEntry, WeightEntry


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required
def dashboard(request):
    weight_form = WeightEntryForm(prefix="weight")
    food_form = FoodEntryForm(prefix="food")

    if request.method == "POST":
        if request.POST.get("form_type") == "weight":
            weight_form = WeightEntryForm(request.POST, prefix="weight")
            if weight_form.is_valid():
                entry = weight_form.save(commit=False)
                entry.user = request.user
                entry.save()
                return redirect("dashboard")

        elif request.POST.get("form_type") == "food":
            food_form = FoodEntryForm(request.POST, prefix="food")
            if food_form.is_valid():
                entry = food_form.save(commit=False)
                entry.user = request.user
                entry.save()
                return redirect("dashboard")

    weights = WeightEntry.objects.filter(user=request.user)
    foods = FoodEntry.objects.filter(user=request.user)

    return render(request, "tracker/dashboard.html", {
        "weight_form": weight_form,
        "food_form": food_form,
        "weights": weights,
        "foods": foods,
    })
