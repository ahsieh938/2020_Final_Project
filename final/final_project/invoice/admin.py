from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone')


class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_num', 'po_num', 'customer', 'invoice_date', 'ship_date')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'product', 'user_num', 'quantity', 'amount', 'contract_start', 'contract_end')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Carrier, CarrierAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ContractType, ContractTypeAdmin)

