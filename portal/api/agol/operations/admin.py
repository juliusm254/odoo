from django.contrib import admin
<<<<<<< Updated upstream
from operations.models import Labinspection
=======
from operations.models import Labinspection, SafetyChecklistQuestion
>>>>>>> Stashed changes

# Register your models here.
@admin.register(Labinspection)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['order','pressure', 'oxygen','nitrogen', 'methane']

<<<<<<< Updated upstream
=======
@admin.register(SafetyChecklistQuestion)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = []

>>>>>>> Stashed changes
# Register your models here.
