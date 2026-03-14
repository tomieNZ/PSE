import json
import os
import markdown as md
from pathlib import Path
from django.conf import settings
from django.shortcuts import render, redirect


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)


def classify_bmi(bmi):
    if bmi < 20:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    else:
        return "Overweight"


def bmi_view(request):
    bmi = None
    category = None
    weight = ""
    height = ""

    if request.method == "POST":
        try:
            weight = float(request.POST["weight"])
            height = float(request.POST["height"])
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
        except (ValueError, ZeroDivisionError, KeyError):
            category = "Invalid input"

    return render(request, "bmi.html", {
        "bmi": bmi,
        "category": category,
        "weight": weight,
        "height": height,
    })


def _load_bookings():
    path = settings.BOOKINGS_FILE
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def _save_bookings(bookings):
    with open(settings.BOOKINGS_FILE, "w") as f:
        json.dump(bookings, f, indent=2)


def appointment_view(request):
    bookings = _load_bookings()
    success = False
    errors = {}

    if request.method == "POST":
        student = request.POST.get("student", "").strip()
        lecturer = request.POST.get("lecturer", "").strip()
        date = request.POST.get("date", "").strip()
        time = request.POST.get("time", "").strip()
        reason = request.POST.get("reason", "").strip()

        if not student:
            errors["student"] = "Student name is required."
        if not lecturer:
            errors["lecturer"] = "Lecturer name is required."
        if not date:
            errors["date"] = "Date is required."
        if not time:
            errors["time"] = "Time is required."

        if not errors:
            booking = {
                "student": student,
                "lecturer": lecturer,
                "date": date,
                "time": time,
                "reason": reason,
            }
            bookings.append(booking)
            _save_bookings(bookings)
            return redirect("/appointment/?success=1")

    success = request.GET.get("success") == "1"
    bookings = _load_bookings()

    time_slots = []
    for hour in range(9, 17):
        time_slots.append(f"{hour:02d}:00")
        time_slots.append(f"{hour:02d}:30")
    time_slots.append("17:00")

    return render(request, "appointment.html", {
        "bookings": bookings,
        "success": success,
        "errors": errors,
        "time_slots": time_slots,
    })


def plan_view(request):
    error = None

    if request.method == "POST":
        try:
            weight = float(request.POST["weight"])
            height = float(request.POST["height"])
            age = int(request.POST["age"])
            gender = request.POST["gender"]

            from promptflow.client import PFClient
            pf = PFClient()

            flow_path = Path(settings.BASE_DIR) / "flows" / "diet_exercise_plan"
            result = pf.test(
                flow=str(flow_path),
                inputs={
                    "weight": weight,
                    "height": height,
                    "age": age,
                    "gender": gender,
                },
            )

            diet_html = md.markdown(result["diet_plan"], extensions=["extra"])
            exercise_html = md.markdown(result["exercise_plan"], extensions=["extra"])

            return render(request, "plan_result.html", {
                "bmi": result["bmi"],
                "category": result["category"],
                "age": age,
                "gender": gender,
                "diet_plan": diet_html,
                "exercise_plan": exercise_html,
            })

        except Exception as e:
            error = str(e)

    return render(request, "plan_form.html", {"error": error})
