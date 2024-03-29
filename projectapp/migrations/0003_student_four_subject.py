# Generated by Django 2.2.7 on 2019-12-01 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_student_subject_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_four_subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fourth_subject', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=30)),
                ('studentformsave', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Std_fours_subject_list', to='projectapp.student_form')),
            ],
        ),
    ]
