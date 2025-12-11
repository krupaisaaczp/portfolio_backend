from django.urls import path
from .views import (
    ProjectListAPIView, ProjectDetailAPIView,
    ContactCreateAPIView
)

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view()),
    path('projects/<slug:slug>/', ProjectDetailAPIView.as_view()),

    path('contact/', ContactCreateAPIView.as_view()),
]
