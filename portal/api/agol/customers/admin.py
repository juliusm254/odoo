from django.contrib import admin
from customers.models import Customer, Order, CustomerTruck, CustomerDriver, CustomerTrailer, Vehicle, Driver

# Register your models here.
@admin.register(Customer)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','name', 'email', 'odoo_customer_id']
  search_fields = ('name',)

@admin.register(Driver)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','national_id', 'name']
  search_fields = ('national_id',)

@admin.register(Vehicle)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['registration', 'transporter', 'epra_no']

@admin.register(CustomerTruck)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = []

@admin.register(CustomerDriver)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = []

@admin.register(CustomerTrailer)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = []

# Register your models here.
@admin.register(Order)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id', 'customer','destination', 'order_quantity', 'order_status', 'driver', 'truck', 'trailer']
