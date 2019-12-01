from django.contrib import admin
from .models import student_form, Student_Profile, student_subject_list



# Register your models here.
admin.site.register(student_form)

admin.site.register(Student_Profile)

admin.site.register(student_subject_list)