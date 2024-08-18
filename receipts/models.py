from django.db import models

class Receipt(models.Model):
    # Basic Receipt Information
    date_time = models.DateTimeField(null=True, blank=True)  # Date and Time of the transaction
    store_name = models.CharField(max_length=255, null=True, blank=True)  # Name of the store or business
    store_location = models.CharField(max_length=255, null=True, blank=True)  # Address of the store
    transaction_number = models.CharField(max_length=100, unique=True, null=True, blank=True)  # Unique transaction identifier

    # Transaction Details
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Total amount spent
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Tax paid
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Tax rate, if applicable
    payment_method = models.CharField(max_length=50, null=True, blank=True)  # Method of payment (e.g., credit card, cash)
    
    # Itemized Purchases
    itemized_purchases = models.TextField(null=True, blank=True)  # Breakdown of items or services purchased

    # Receipt Metadata
    receipt_category = models.CharField(max_length=100, null=True, blank=True)  # Categorization of the receipt (e.g., business, personal)
    keywords_tags = models.CharField(max_length=255, null=True, blank=True)  # Tags for easy searching
    scan_date = models.DateField(null=True, blank=True)  # Date the receipt was scanned into the system

    # Receipt Image Data
    scanned_image = models.ImageField(upload_to='receipts/')  # High-resolution image of the receipt
    ocr_data = models.TextField(null=True, blank=True)  # OCR extracted text data

    # Vendor Details
    vendor_contact_info = models.CharField(max_length=255, null=True, blank=True)  # Vendor's contact details
    vendor_identification_number = models.CharField(max_length=100, null=True, blank=True)  # Vendor or merchant ID

    # Legal/Compliance Data
    tax_identification_numbers = models.CharField(max_length=100, null=True, blank=True)  # VAT or other tax IDs
    regulatory_details = models.TextField(null=True, blank=True)  # Any legal requirements for record-keeping

    # Additional Notes
    notes_comments = models.TextField(null=True, blank=True)  # Space for any manual notes or details

    def __str__(self):
        return f'Receipt from {self.store_name} on {self.date_time} - Total: {self.total_amount}'