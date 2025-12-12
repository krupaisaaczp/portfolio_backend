from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.core.mail import send_mail

from .models import Project, ContactMessage
from .serializers import ProjectSerializer, ContactSerializer


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    lookup_field = 'slug'
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        data = serializer.save()

        subject = f"New Contact Message from {data.first_name} {data.last_name}"
        message = (
            f"Name: {data.first_name} {data.last_name}\n"
            f"Email: {data.email}\n"
            f"Phone: {data.phone}\n\n"
            f"Message:\n{data.message}"
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
