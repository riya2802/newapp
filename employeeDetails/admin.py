from django.contrib import admin
from .models import employee,employeeFamily,employeeChildren,employeeHealth,Job,Contact


admin.site.register(employee)
admin.site.register(employeeFamily)
admin.site.register(employeeChildren)
admin.site.register(employeeHealth)
admin.site.register(Job)
admin.site.register(Contact)
# Register your models here.
