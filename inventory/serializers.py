from rest_framework import serializers
from .models import Medicine, StockBatch

class StockBatchSerializer(serializers.ModelSerializer):
    days_until_expiry = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    class Meta:
        model = StockBatch
        fields = ['id', 'batch_number', 'quantity', 'unit_price', 'production_date', 'expiry_date', 'days_until_expiry', 'status']

class MedicineSerializer(serializers.ModelSerializer):
    batches = StockBatchSerializer(many=True, read_only=True)

    class Meta:
        model = Medicine
        fields = ['id', 'name', 'scientific_name', 'barcode', 'batches']