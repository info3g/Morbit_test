# Generated by Django 3.2.9 on 2021-12-09 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll_no',
            new_name='rollno',
        ),
    ]
