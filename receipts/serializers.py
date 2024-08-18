from rest_framework import serializers
from .models import Receipt

class ReceiptImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['scanned_image']