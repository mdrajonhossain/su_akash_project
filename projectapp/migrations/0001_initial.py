# Generated by Django 2.2.7 on 2019-11-28 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=30)),
                ('dateofbirth', models.DateField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('departsubject', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_Profile_images', models.ImageField(upload_to='std_Profile_images_file/')),
                ('studentformsave', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Std_Profile', to='projectapp.student_form')),
            ],
        ),
    ]
