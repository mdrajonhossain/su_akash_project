from django.db import models

# Create your models here.

class student_form(models.Model):	
    applicant_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    dateofbirth = models.DateField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    departsubject = models.CharField(max_length=30)
    
    def __str__(self):
    	return self.applicant_name

  
class Student_Profile(models.Model):	 
	studentformsave = models.OneToOneField(student_form, on_delete=models.CASCADE, related_name='Std_Profile')
	std_Profile_images = models.ImageField(upload_to='std_Profile_images_file/')



class student_subject_list(models.Model):
    studentformsave = models.OneToOneField(student_form, on_delete=models.CASCADE, related_name='Std_subject_list')       
    bangla = models.CharField(max_length=30)
    mathmathics = models.CharField(max_length=30)
    english = models.CharField(max_length=30)
    english = models.CharField(max_length=30)
    