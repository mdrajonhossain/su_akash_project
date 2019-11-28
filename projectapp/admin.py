from django.contrib import admin
from .models import student_form, Student_Profile



# Register your models here.
admin.site.register(student_form)

admin.site.register(Student_Profile)