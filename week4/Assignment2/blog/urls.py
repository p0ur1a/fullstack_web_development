# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path("", views.student_list, name="student_list"),

    path('', views.student_list, name='student_list'),

]