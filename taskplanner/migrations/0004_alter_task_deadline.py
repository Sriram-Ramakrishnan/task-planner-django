# Generated by Django 4.1.3 on 2022-12-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskplanner', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
