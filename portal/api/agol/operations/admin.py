from django.contrib import admin
from operations.models import Labinspection

# Register your models here.
@admin.register(Labinspection)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['order','pressure', 'oxygen','nitrogen', 'methane']

# Register your models here.
