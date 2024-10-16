from django.urls import path
from projects import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<str:pk>/", views.project_detail, name="project_detail"),
]
