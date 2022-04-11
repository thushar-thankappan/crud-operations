from django.contrib import admin
from .models import Position, Employee

class PositionAdmin(admin.ModelAdmin):
    list_display=['id','title']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','firstname', 'lastname','emp_no', 'mobile', 'position', 'place']

admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
