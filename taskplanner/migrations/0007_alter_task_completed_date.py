# Generated by Django 4.1.3 on 2022-12-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskplanner', '0006_task_completed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]