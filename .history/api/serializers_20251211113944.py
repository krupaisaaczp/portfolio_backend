from .models import ContactMessage
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
