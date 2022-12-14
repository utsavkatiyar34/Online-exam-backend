# Generated by Django 4.1.3 on 2022-11-17 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0005_delete_course'),
        ('cources', '0010_alter_assigned_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('Score_id', models.AutoField(primary_key=True, serialize=False)),
                ('Score', models.IntegerField(unique=True)),
                ('Student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server_app.student')),
                ('Test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cources.test')),
            ],
        ),
    ]
