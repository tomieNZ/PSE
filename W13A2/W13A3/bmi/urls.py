from django.urls import path
from . import views

urlpatterns = [
    path("", views.bmi_view, name="bmi"),
    path("appointment/", views.appointment_view, name="appointment"),
    path("plan/", views.plan_view, name="plan"),
]
