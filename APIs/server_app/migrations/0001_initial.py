# Generated by Django 4.1.3 on 2022-11-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=75)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Designation', models.CharField(max_length=100)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
