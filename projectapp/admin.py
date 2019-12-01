from django.contrib import admin
from .models import student_form, Student_Profile, student_subject_list, student_four_subject, student_result_sheet



# student information
admin.site.register(student_form)
admin.site.register(Student_Profile)
admin.site.register(student_subject_list)
admin.site.register(student_four_subject)
admin.site.register(student_result_sheet)



# admin panal design site
admin.site.site_header = "Student Management System is Admin Panal"
admin.site.site_title = "Student Management System"
admin.site.index_title = "Admin"

