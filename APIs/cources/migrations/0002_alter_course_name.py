# Generated by Django 4.1.3 on 2022-11-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
