import os
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from receipts.models import Receipt
from django.core.files.uploadedfile import SimpleUploadedFile

class ReceiptImageUploadTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')

    def test_upload_receipt_image(self):
        url = reverse('upload_receipt')
        image_path = os.path.join(os.path.dirname(__file__), 'images', 'image.png')
        self.assertTrue(os.path.exists(image_path), f"File {image_path} does not exist.")
        with open(image_path, 'rb') as image_file:
            image = SimpleUploadedFile("image.png", image_file.read(), content_type="image/png")
            data = {'scanned_image': image}
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)