from django.contrib import admin
from blog.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)