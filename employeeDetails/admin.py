from django.contrib import admin
from .models import employee,employeeFamily,employeeChildren,employeeHealth,Job,Contact,nationality,country,ethnicity,religion,jobType,jobStatus,workDays,leaveWorkFlow,holiDays,lineManager,level,position,branch,department,bloodGroup,maritalStatus,numberOfChild
admin.site.register(employee)
admin.site.register(employeeFamily)
admin.site.register(employeeChildren)
admin.site.register(employeeHealth)
admin.site.register(Job)
admin.site.register(nationality)
admin.site.register(ethnicity)
admin.site.register(jobType)
admin.site.register(jobStatus)
admin.site.register(workDays)
admin.site.register(leaveWorkFlow)
admin.site.register(holiDays)
admin.site.register(lineManager)
admin.site.register(level)
admin.site.register(position)
admin.site.register(branch)
admin.site.register(department)
admin.site.register(bloodGroup)
admin.site.register(maritalStatus)
admin.site.register(numberOfChild)


# Register your models here.
