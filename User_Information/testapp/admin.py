from django.contrib import admin
from testapp.models import student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','mobile_number','email','userID']
admin.site.register(student, StudentAdmin)