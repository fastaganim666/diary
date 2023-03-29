# Generated by Django 4.1.7 on 2023-03-28 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_taskday_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskday',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='timeday',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='timeday',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time', to='planner.taskday', verbose_name='Время'),
        ),
    ]
