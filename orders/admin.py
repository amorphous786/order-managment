from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_name', 'freight', 'ship_name', 'ship_country', 'created_at']
    list_filter = ['ship_country', 'created_at']
    search_fields = ['order_id', 'customer_name', 'ship_name']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_id', 'customer_name', 'freight')
        }),
        ('Shipping Information', {
            'fields': ('ship_name', 'ship_country')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
