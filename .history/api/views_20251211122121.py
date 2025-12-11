from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from .models import ContactMessage
from .serializers import ContactSerializer

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    lookup_field = 'slug'
    serializer_class = ProjectSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
