from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Medicine, StockBatch
from .serializers import MedicineSerializer, StockBatchSerializer

# --- Dashboard View (Front-End) ---
def dashboard(request):
    batches = StockBatch.objects.select_related('medicine').all()
    
    total_medicines = Medicine.objects.count()
    expired_count = sum(1 for b in batches if b.status == 'EXPIRED')
    near_expiry_count = sum(1 for b in batches if b.status == 'NEAR_EXPIRY')
    fresh_count = sum(1 for b in batches if b.status == 'FRESH')

    context = {
        'batches': batches,
        'total_medicines': total_medicines,
        'expired_count': expired_count,
        'near_expiry_count': near_expiry_count,
        'fresh_count': fresh_count,
    }
    return render(request, 'inventory/dashboard.html', context)


# --- REST API ViewSets (Back-End) ---
class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class StockBatchViewSet(viewsets.ModelViewSet):
    queryset = StockBatch.objects.all()
    serializer_class = StockBatchSerializer

    # Endpoint خاص لجلب الأدوية القريبة من الانتهاء فقط
    @action(detail=False, methods=['get'])
    def near_expiry(self, request):
        near_expiry_batches = [batch for batch in self.get_queryset() if batch.status == 'NEAR_EXPIRY']
        serializer = self.get_serializer(near_expiry_batches, many=True)
        return Response(serializer.data)