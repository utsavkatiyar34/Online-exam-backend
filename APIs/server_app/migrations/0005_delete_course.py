# Generated by Django 4.1.3 on 2022-11-15 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0004_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]