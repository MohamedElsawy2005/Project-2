from django.contrib import admin
from django.utils.html import format_html
from .models import Medicine, StockBatch

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'barcode')
    search_fields = ('name', 'scientific_name', 'barcode')

# إجراء سريع لتصفير الكميات المنتهية الصلاحية
@admin.action(description='تصفير كمية التشغيلات المحددة (إعدام المخزون)')
def mark_as_expired_and_zero(modeladmin, request, queryset):
    updated_count = queryset.update(quantity=0)
    modeladmin.message_user(request, f'تم تصفير كمية {updated_count} تشغيلة بنجاح.')

@admin.register(StockBatch)
class StockBatchAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'batch_number', 'quantity', 'unit_price', 'expiry_date', 'get_days', 'colored_status')
    list_filter = ('expiry_date',)
    search_fields = ('medicine__name', 'batch_number')
    actions = [mark_as_expired_and_zero]  # إضافة الزر للقائمة

    @admin.display(description='الأيام المتبقية')
    def get_days(self, obj):
        return obj.days_until_expiry

    @admin.display(description='حالة الصلاحية')
    def colored_status(self, obj):
        status = obj.status
        if status == 'EXPIRED':
            color = 'red'
            text = 'منتهي الصلاحية'
        elif status == 'NEAR_EXPIRY':
            color = 'orange'
            text = 'قريب الانتهاء'
        else:
            color = 'green'
            text = 'صالح'
        
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            text
        )