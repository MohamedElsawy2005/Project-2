from django.db import models
from django.utils import timezone

class Medicine(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم الدواء")
    scientific_name = models.CharField(max_length=200, blank=True, verbose_name="المادة الفعالة")
    barcode = models.CharField(max_length=100, unique=True, verbose_name="الباركود")

    def __str__(self):
        return self.name

class StockBatch(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='batches', verbose_name="الدواء")
    batch_number = models.CharField(max_length=50, verbose_name="رقم التشغيلة")
    quantity = models.PositiveIntegerField(verbose_name="الكمية")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الوحدة")
    production_date = models.DateField(verbose_name="تاريخ الإنتاج")
    expiry_date = models.DateField(verbose_name="تاريخ انتهاء الصلاحية")

    @property
    def days_until_expiry(self):
        """حساب الأيام المتبقية تلقائياً"""
        today = timezone.now().date()
        return (self.expiry_date - today).days

    @property
    def status(self):
        """تحديد الحالة تلقائياً بناءً على تاريخ اليوم"""
        days = self.days_until_expiry
        if days < 0:
            return "EXPIRED"        # منتهي الصلاحية
        elif days <= 30:
            return "NEAR_EXPIRY"    # قريب الانتهاء
        return "FRESH"              # صالح

    def __str__(self):
        return f"{self.medicine.name} - Batch {self.batch_number} ({self.status})"