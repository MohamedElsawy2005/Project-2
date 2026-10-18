from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'medicines', views.MedicineViewSet)
router.register(r'batches', views.StockBatchViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/', include(router.urls)),
]