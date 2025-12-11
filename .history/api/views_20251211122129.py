from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from .models import ContactMessage
from .serializers import ContactSerializer
from django.core.mail import send_mail
from rest_framework import generics
from .models import ContactMessage
from .serializers import ContactSerializer

class ContactCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        data = serializer.save()

        # Prepare email content
        subject = f"New Contact Message from {data.first_name} {data.last_name}"
        message = (
            f"Name: {data.first_name} {data.last_name}\n"
            f"Email: {data.email}\n"
            f"Phone: {data.phone}\n\n"
            f"Message:\n{data.message}"
        )

        # Send email to you
        send_mail(
            subject,
            message,
            None,  # uses DEFAULT_FROM_EMAIL
            [EMAIL_HOST_USER],
            fail_silently=False
        )


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
