# Generated by Django 5.0.1 on 2024-01-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_jobseekerprofile_applicantprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprofile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
