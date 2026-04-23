from django.contrib import admin
from ecommerceapp.models import Contact, Product, Orders, OrderUpdate

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name', 'category', 'subcategory']   # 🔍 Search box
    list_display = ['product_name', 'category', 'subcategory', 'price']  # 📋 Table columns
    list_filter = ['category', 'subcategory']   # 🔽 Right-side filter panel
    ordering = ['product_name']   # Sort A to Z by default

class OrdersAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'oid']   # 🔍 Search orders by name/email
    list_display = ['name', 'email', 'amount', 'paymentstatus', 'city']
    list_filter = ['paymentstatus']

admin.site.register(Contact)
admin.site.register(Product, ProductAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderUpdate)