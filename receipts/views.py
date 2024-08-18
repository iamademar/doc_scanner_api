from rest_framework import generics, status
from rest_framework.response import Response
from .models import Receipt
from .serializers import ReceiptImageUploadSerializer

class ReceiptImageUploadView(generics.CreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptImageUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)  # Log the validation errors
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)